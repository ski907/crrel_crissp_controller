New users need to manually place the CSP2D_Mainprog.exe and CSP2D_Mainprog.123 files in the ./simulations/ folder (it has to go there becasue the exe produces incomplete filenames if the path to the simulation dir is too long)

Update paraview_path in ./src/paraview_config.yaml to the local path of your paraview exe, the paraview_pvpython_path isn't used currently (headless mode) but you can update if you want

This works in Python 3.12.4. the requirements.txt file in ./src/ should have everything needed to run the code so you can do this:

cd ./src/
conda create --name ccc python=3.12.4
conda activate ccc
conda install pip
pip install -r requirements.txt

python ccc.py
