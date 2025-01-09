import os
import glob
import math
import json
import yaml
import numpy as np
import pandas as pd
import rasterio
import rasterio.mask
from rasterio.transform import from_origin
from shapely.geometry import Polygon, MultiPoint, mapping
from shapely.ops import unary_union
from scipy.spatial import Delaunay
from scipy.interpolate import griddata

from .parse_plts import parse_plt

def get_active_sim(root_dir):
    """Get the currently active simulation from the configuration file."""
    config_path = os.path.join(root_dir, 'active_sim.yaml')
    config = get_yaml_config(config_path)
    return config.get('active_sim')

def get_yaml_config(config_path):
    """Read a YAML configuration file."""
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

def concave_hull_delaunay(points, max_edge=105):
    """
    Creates a 'concave hull' from a set of 2D points by:
      1. Delaunay Triangulation
      2. Removing triangles with any edge > max_edge
      3. Taking the union of the remaining triangles

    Parameters
    ----------
    points : list of (x, y) tuples
    max_edge : float
        The maximum allowed edge length in the triangulation.

    Returns
    -------
    A Shapely Polygon or MultiPolygon representing the hull.
    """
    if len(points) < 4:
        return MultiPoint(points).convex_hull

    pts = np.array(points)
    tri = Delaunay(pts)

    kept_polygons = []
    for simplex in tri.simplices:
        coords = pts[simplex]
        # Check each of the 3 edges in the triangle
        if all(np.linalg.norm(coords[i] - coords[(i + 1) % 3]) <= max_edge for i in range(3)):
            kept_polygons.append(Polygon(coords))

    if kept_polygons:
        return unary_union(kept_polygons)
    else:
        return MultiPoint(points).convex_hull


def generate_tiffs(df, concave_hull, output_folder, var_names=None, resolution=50.0):
    """
    Generate TIFFs for each variable in `var_names` (or all numeric columns if `var_names` is None).
    The TIFFs are saved in `output_folder`. Then each TIFF is clipped using `concave_hull`.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame containing at least "Points:0", "Points:1", and variable columns.
    concave_hull : shapely Polygon
        Polygon used for clipping.
    output_folder : str
        Folder to store the generated TIFFs (full and clipped).
    var_names : list of str or None
        If None, will attempt to use all columns except "Points:0", "Points:1".
    resolution : float
        The cell size for the output raster.
    """
    # Identify columns for X and Y
    x_col = "X" 
    y_col = "Y"

    # If var_names is not provided, pick all columns except X and Y
    if var_names is None:
        var_names = [col for col in df.columns if col not in [x_col, y_col]]

    x = df[x_col].values
    y = df[y_col].values

    # Compute bounding box of data
    x_min, x_max = x.min(), x.max()
    y_min, y_max = y.min(), y.max()

    # Number of cells in each direction
    nx = int(math.ceil((x_max - x_min) / resolution))
    ny = int(math.ceil((y_max - y_min) / resolution))

    # Create grid for interpolation
    xi = np.linspace(x_min, x_min + nx * resolution, nx)
    # For Y, let's go top-down
    yi = np.linspace(y_max, y_max - ny * resolution, ny)
    grid_x, grid_y = np.meshgrid(xi, yi)

    # Define a transform for Rasterio
    transform = from_origin(xi[0], yi[0], resolution, resolution)

    # Generate a TIFF per variable
    for var in var_names:
        z = df[var].values

        # Interpolate onto the grid
        grid_z = griddata((x, y), z, (grid_x, grid_y), method="linear")

        # If interpolation fails in some areas, it returns nan
        # You could also use 'nearest' or 'cubic' interpolation

        # Full raster path
        out_raster = os.path.join(output_folder, f"{var}_full.tif")
        # Clipped raster path
        out_raster_clipped = os.path.join(output_folder, f"{var}_clipped.tif")

        # 1. Write the full raster
        with rasterio.open(
            out_raster,
            "w",
            driver="GTiff",
            height=grid_z.shape[0],
            width=grid_z.shape[1],
            count=1,
            dtype=str(grid_z.dtype),
            crs="ESRI:103076",  # or another CRS
            transform=transform,
            nodata=np.nan
        ) as dst:
            dst.write(grid_z, 1)

        # 2. Clip the raster using the concave hull
        clip_shapes = [concave_hull.__geo_interface__]
        with rasterio.open(out_raster) as src:
            clipped_data, clipped_transform = rasterio.mask.mask(
                src, shapes=clip_shapes, crop=True, nodata=np.nan
            )
            clipped_meta = src.meta.copy()
            clipped_meta.update({
                "height": clipped_data.shape[1],
                "width": clipped_data.shape[2],
                "transform": clipped_transform,
                "nodata": np.nan
            })

            # Because it's a single band, we can squeeze
            clipped_data = clipped_data.squeeze()

            with rasterio.open(out_raster_clipped, "w", **clipped_meta) as dst:
                dst.write(clipped_data, 1)

        os.remove(out_raster)


def main(root_directory):
    # Adjust root_directory to your actual path, e.g., "../../"
    #root_directory = "../../"
    
    # 1. Get the active simulation name (e.g. "StClair")
    active_simulation = get_active_sim(root_directory)
    
    # 2. Build paths
    out_dir = os.path.join(root_directory, "simulations", active_simulation, "out")
    post_process_dir = os.path.join(root_directory, "simulations", active_simulation, "post_process")
    os.makedirs(post_process_dir, exist_ok=True)

    # 3. Collect all .plt files
    plt_files = sorted(glob.glob(os.path.join(out_dir, "*.plt")))
    if not plt_files:
        print("No .plt files found in:", out_dir)
        return

    # 4. Create hull from the first .plt file (only once)
    first_plt = plt_files[0]
    df_first = parse_plt(first_plt)
    
    # Convert the first PLT's XY columns into a list of (x, y) for the hull
    x = df_first["X"].values
    y = df_first["Y"].values
    points = list(zip(x, y))

    # Concave hull with a max_edge threshold
    hull = concave_hull_delaunay(points, max_edge=105)

    # (Optional) Save hull to a GeoJSON for future reference
    hull_file = os.path.join(post_process_dir, "concave_hull.geojson")
    with open(hull_file, "w") as f:
        json.dump(mapping(hull), f)
    print(f"Concave hull saved to: {hull_file}")

    # 5. Loop over each .plt file, parse, and generate TIFFs
    for plt_path in plt_files:
        # e.g., "StClair001.plt" -> base_name "StClair001"
        base_name = os.path.splitext(os.path.basename(plt_path))[0]

        # Create a subfolder in post_process for each .plt
        subfolder = os.path.join(post_process_dir, base_name)
        os.makedirs(subfolder, exist_ok=True)

        df = parse_plt(plt_path)

        # Generate TIFFs for each column in the .plt file
        # (except X and Y columns, unless you specify var_names explicitly)
        generate_tiffs(df, hull, subfolder)

    print("All .plt files have been processed.")


if __name__ == "__main__":
    main()
