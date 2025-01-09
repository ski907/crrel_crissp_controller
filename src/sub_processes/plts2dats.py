import os
import shutil
import yaml

def process_output(sim_folder):
    """
    Processes the simulation output by converting .plt files in the "out" folder
    to .dat files in the "para_dats" folder.

    Args:
        sim_folder (str): The path to the simulation folder.
    """
    print(f"Processing output for {sim_folder}...")

    # Define source and destination directories
    source_dir = os.path.join(sim_folder, "out")
    destination_dir = os.path.join(sim_folder, "para_dats")

    # Step 1: Clear contents of para_dats, but keep the folder
    if os.path.exists(destination_dir):
        for file_name in os.listdir(destination_dir):
            file_path = os.path.join(destination_dir, file_name)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")

    # Step 2: Create para_dats if it doesn't exist
    os.makedirs(destination_dir, exist_ok=True)

    # Step 3: Convert .plt files to .dat and copy them to para_dats
    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist. Skipping processing.")
        return

    for file_name in os.listdir(source_dir):
        if file_name.endswith('.plt'):
            source_file = os.path.join(source_dir, file_name)
            new_file_name = os.path.splitext(file_name)[0] + '.dat'
            destination_file = os.path.join(destination_dir, new_file_name)

            # Copy and rename the file
            try:
                shutil.copy(source_file, destination_file)
                print(f"Copied and renamed: {source_file} to {destination_file}")
            except Exception as e:
                print(f"Failed to copy {source_file}. Reason: {e}")

    print("Processing completed: All .plt files have been copied and renamed to .dat.")

def get_active_sim(root_dir):
    """
    Retrieves the active simulation folder from active_sim.yaml.

    Args:
        root_dir (str): The root directory of the project.

    Returns:
        str: Path to the active simulation folder.
    """
    config_path = os.path.join(root_dir, 'active_sim.yaml')
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    
    active_sim = config.get('active_sim')
    if not active_sim:
        raise ValueError("No active simulation defined in active_sim.yaml.")
    
    return os.path.join(root_dir, "simulations", active_sim)

if __name__ == "__main__":
    # Default to processing the active simulation
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    try:
        sim_folder = get_active_sim(project_root)
        process_output(sim_folder)
    except Exception as e:
        print(f"Error: {e}")
