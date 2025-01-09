import os
import yaml
import subprocess

from sub_processes.plts2dats import process_output
from sub_processes.process_rasters import main as process_rasters_main


def get_paraview_path():
    """
    Read the path to the Paraview executable from 'paraview_config.yaml',
    located in the same directory as this file.
    """
    config_path = os.path.join(os.path.dirname(__file__), "paraview_config.yaml")
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Paraview configuration file not found: {config_path}")

    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    return config.get('paraview_path')


def get_yaml_config(config_path):
    """
    Load a YAML configuration file and return it as a dictionary.
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)


def write_yaml_config(config_path, data):
    """
    Write the given dictionary `data` to a YAML configuration file.
    """
    with open(config_path, 'w') as file:
        yaml.dump(data, file)


def get_active_sim(root_dir):
    """
    Retrieve the currently active simulation name from 'active_sim.yaml'
    in the specified `root_dir`.
    """
    config_path = os.path.join(root_dir, 'active_sim.yaml')
    config = get_yaml_config(config_path)
    return config.get('active_sim')


def get_active_file_name(root_dir):
    """
    Retrieve the active simulation's file name from 'active_sim.yaml'
    in the specified `root_dir`.
    """
    config_path = os.path.join(root_dir, 'active_sim.yaml')
    config = get_yaml_config(config_path)
    return config.get('active_file_name')


def set_active_sim(root_dir, sim_name):
    """
    Set the currently active simulation (`sim_name`) in 'active_sim.yaml'.
    """
    config_path = os.path.join(root_dir, 'active_sim.yaml')
    config = {'active_sim': sim_name}
    write_yaml_config(config_path, config)


def switch_simulation(root_dir, sim_name):
    """
    Switch the active simulation by updating 'active_sim.yaml' to `sim_name`.
    Validates that `sim_name` folder exists in 'simulations/' before switching.
    """
    sim_folder = os.path.join(root_dir, "simulations", sim_name)
    if not os.path.exists(sim_folder):
        raise FileNotFoundError(f"Simulation folder {sim_name} does not exist.")

    set_active_sim(root_dir, sim_name)
    print(f"Active simulation switched to '{sim_name}'.")


def run_crissp2d_for_active_sim(root_dir):
    """
    Run CRISSP2D for the active simulation by:
      1) Getting the active simulation/folder.
      2) Locating and validating required paths.
      3) Executing the batch file that runs CSP2D_Mainprog.exe in a new window.
    """
    sim_name = get_active_sim(root_dir)
    sim_folder = os.path.join(root_dir, "simulations", sim_name)
    if not os.path.exists(sim_folder):
        raise FileNotFoundError(f"Simulation folder '{sim_name}' not found in '{sim_folder}'.")

    print(f"Running workflow for '{sim_name}'...")

    try:
        file_name  = get_active_file_name(root_dir)  
        batch_file = os.path.abspath(os.path.join("sub_processes", "run_prog.bat"))
        exe_path   = os.path.abspath(os.path.join(sim_folder, "..", "CSP2D_Mainprog.exe"))
        root_path  = os.path.abspath(os.path.join(sim_folder, "..", ".."))

        # Log relevant paths for clarity
        print(f"Batch file:      {batch_file}")
        print(f"Executable path: {exe_path}")
        print(f"Root path:       {root_path}")
        print(f"Simulation name: {sim_name}")
        print(f"File name:       {file_name}")

        # Construct the command and run it in a separate window via 'start cmd /k'
        command = f'start cmd /k ""{batch_file}" "{sim_name}" "{file_name}" "{root_path}" "{exe_path}""'
        print(f"Executing command: {command}")

        working_dir = os.path.dirname(exe_path)
        subprocess.run(
            command,
            check=False,
            shell=True,
            cwd=working_dir,
            stderr=subprocess.DEVNULL
        )

        print("\n**********************************************************************")
        print("Batch File Executed")
        print(f"Controller has attempted to kick off Simulation for '{sim_name}'. Running in separate window...")
        print("Post-processing can be done mid-run if there are .plt files in the out folder.")

    except Exception as e:
        print(f"Error during workflow: {e}")


def post_process_paraview(sim_folder, root_dir):
    """
    Orchestrate post-processing steps:
      1) Convert .plt to .dat (via plts2dats).
      2) Run a Paraview script for visualization (headless or interactive).
    """
    try:
        print(f"Starting post-processing for '{sim_folder}'...")

        prefix = get_active_file_name(root_dir)
        print(f"Derived prefix: {prefix}")

        # Step 1: .plt -> .dat conversion
        print("Running plts2dats processing...")
        process_output(sim_folder)
        print("plts2dats processing completed.")

        # Step 2: Run Paraview script
        print("Running Paraview script...")
        paraview_script_path = os.path.join(os.path.dirname(__file__), "sub_processes", "paraview_script.py")
        paraview_path = get_paraview_path()

        if not os.path.exists(paraview_path):
            raise FileNotFoundError(f"Paraview executable not found: {paraview_path}")

        # Example: open new window, run Paraview with the given script
        # command = f'"{paraview_path}" {paraview_script_path} {sim_folder} {prefix}'
        # Or run with --script parameter:
        command = f'start cmd /k "{paraview_path}" --script={paraview_script_path}'
        print(f"Executing command: {command}")

        subprocess.run(command, check=True, shell=True)
        print("Paraview script command executed successfully. Running in separate window.")

        print("Post-processing completed successfully.")

    except Exception as e:
        print(f"Error during post-processing: {e}")


def print_logo():
    """Print a stylized ASCII logo for CRISSP2D."""
    logo = r"""
 ______   ______   ______   ______   __                                                     
/\  ___\ /\  == \ /\  == \ /\  ___\ /\ \                                                    
\ \ \____\ \  __< \ \  __< \ \  __\ \ \ \____                                               
 \ \_____\\ \_\ \_\\ \_\ \_\\ \_____\\ \_____\                                              
 _\/_____/_\/_/_/_/_\/_/_/_/_\/_____/_\/_____/__                                            
/\  ___\ /\  == \ /\ \ /\  ___\ /\  ___\ /\  == \                                           
\ \ \____\ \  __< \ \ \\ \___  \\ \___  \\ \  _-/                                           
 \ \_____\\ \_\ \_\\ \_\\/\_____\\/\_____\\ \_\                                             
 _\/_____/_\/_/_/_/_\/_/_\/_____/_\/_____/_\/_/_____   __       __       ______   ______    
/\  ___\ /\  __ \ /\ "-.\ \ /\__  _\/\  == \ /\  __ \ /\ \     /\ \     /\  ___\ /\  == \   
\ \ \____\ \ \/\ \\ \ \-.  \\/_/\ \/\ \  __< \ \ \/\ \\ \ \____\ \ \____\ \  __\ \ \  __<   
 \ \_____\\ \_____\\ \_\\"\_\  \ \_\ \ \_\ \_\\ \_____\\ \_____\\ \_____\\ \_____\\ \_\ \_\ 
  \/_____/ \/_____/ \/_/ \/_/   \/_/  \/_/ /_/ \/_____/ \/_____/ \/_____/ \/_____/ \/_/ /_/ 
    """
    print(logo)


def process_output_to_tiff(root_directory):
    """
    Invoke the 'process_rasters.py' main function to generate TIFFs from .plt data.
    """
    print("Processing data to rasters...")
    process_rasters_main(root_directory)


def main():
    """Main function for running the overall CRISSP2D workflow."""
    root_directory = "../"  # Adjust if needed
    print_logo()

    while True:
        sim_name = get_active_sim(root_directory)
        print(f"\nCurrent Simulation: {sim_name}")
        print("Options:")
        print("1. Run active simulation in CRISSP2D")
        print("2. Switch active simulation")
        print("3. Run Post-Process in Paraview")
        print("4. Process data to rasters")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                run_crissp2d_for_active_sim(root_directory)
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '2':
            new_sim_name = input("Enter simulation name to activate: ")
            try:
                switch_simulation(root_directory, new_sim_name)
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '3':
            # Post-process in ParaView
            try:
                sim_folder = os.path.join(root_directory, "simulations", sim_name)
                if not os.path.exists(sim_folder):
                    raise FileNotFoundError(f"Simulation folder '{sim_name}' not found.")
                post_process_paraview(sim_folder, root_directory)
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '4':
            # Process data to TIFF
            try:
                process_output_to_tiff(root_directory)
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '5':
            print("Exiting.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
