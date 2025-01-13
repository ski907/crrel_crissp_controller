# trace generated using paraview version 5.9.1

#### import the simple module from the paraview
from paraview.simple import *
import os

ResetSession()
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

current_directory = os.path.dirname(os.path.abspath(__file__))
directory = os.path.join(current_directory, "para_dats")
prefix = 'StClair'
extension = '.dat'

# Generate the list of files
file_list = [
    os.path.join(directory, f)
    for f in sorted(os.listdir(directory))
    if f.startswith(prefix) and f.endswith(extension)
]

# Pass the file list to TecplotReader
stClair = TecplotReader(
    registrationName='StClair*',
    FileNames=file_list
)


stClair.DataArrayStatus = ['Node #', 'W.S.Elev.']

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
stClairDisplay = Show(stClair, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
stClairDisplay.Representation = 'Surface'


# reset view to fit data
renderView1.ResetCamera(False, 0.9)

#changing interaction mode based on data extents
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [4155852.875, 148937.76953125, 136071.844140625]
renderView1.CameraFocalPoint = [4155852.875, 148937.76953125, 0.0]

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# create a query selection
QuerySelect(QueryString='(in1d(Node, [129,2731,4129]))', FieldType='POINT', InsideOut=0)

# create a new 'Extract Selection'
extractSelection1 = ExtractSelection(registrationName='ExtractSelection1', Input=stClair)

# show data in view
extractSelection1Display = Show(extractSelection1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
extractSelection1Display.Representation = 'Surface'

# hide data in view
Hide(stClair, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# Save the extracted selection to a .csv file
output_file = os.path.join(current_directory, 'post_process/extracted_selection.csv')
SaveData(output_file, proxy=extractSelection1)
