# trace generated using paraview version 5.9.1

#### import the simple module from the paraview
from paraview.simple import *

import os
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


stClair.DataArrayStatus = ['W.S.Elev.', 'Node #', 'Ice Concentration', 'Ice Thickness', 'Ice Velocity Ui', 'Vi', 'Ice Vel. Mag.', 'Water Vel. Uw', 'Vw', 'Ww[=0]', 'Water Vel. Mag.', 'Water Depth', 'Froude Number', 'Water Temperature', 'Surface Water Temp.', 'Frazil Conc.', 'Surface Ice Thickness', 'Frazil Ice Thickness', 'Solid Crust Thickness', 'Anchor Ice Thickness', 'Undercover Ice Thickness', 'Bed Elev.', 'Top of Ice', 'Bottom of Ice', 'Border Ice Index', 'Ice Type']

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
stClairDisplay.ColorArrayName = [None, '']
stClairDisplay.SelectTCoordArray = 'None'
stClairDisplay.SelectNormalArray = 'None'
stClairDisplay.SelectTangentArray = 'None'
stClairDisplay.OSPRayScaleArray = 'Anchor Ice Thickness'
stClairDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
stClairDisplay.SelectOrientationVectors = 'None'
stClairDisplay.ScaleFactor = 4061.8460937500004
stClairDisplay.SelectScaleArray = 'Anchor Ice Thickness'
stClairDisplay.GlyphType = 'Arrow'
stClairDisplay.GlyphTableIndexArray = 'Anchor Ice Thickness'
stClairDisplay.GaussianRadius = 203.09230468750002
stClairDisplay.SetScaleArray = ['POINTS', 'Anchor Ice Thickness']
stClairDisplay.ScaleTransferFunction = 'PiecewiseFunction'
stClairDisplay.OpacityArray = ['POINTS', 'Anchor Ice Thickness']
stClairDisplay.OpacityTransferFunction = 'PiecewiseFunction'
stClairDisplay.DataAxesGrid = 'GridAxesRepresentation'
stClairDisplay.PolarAxes = 'PolarAxesRepresentation'
stClairDisplay.ScalarOpacityUnitDistance = 2092.252540707858
stClairDisplay.OpacityArrayName = ['POINTS', 'Anchor Ice Thickness']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
stClairDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
stClairDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera()

#changing interaction mode based on data extents
renderView1.CameraPosition = [4155852.875, 148937.76953125, 10000.0]
renderView1.CameraFocalPoint = [4155852.875, 148937.76953125, 0.0]
renderView1.CameraViewUp = [0.0, 1.0, 0.0]

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(stClairDisplay, ('POINTS', 'W.S.Elev.'))

# rescale color and/or opacity maps used to include current data range
stClairDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
stClairDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'WSElev'
wSElevLUT = GetColorTransferFunction('WSElev')

# get opacity transfer function/opacity map for 'WSElev'
wSElevPWF = GetOpacityTransferFunction('WSElev')

# create a new 'SplineSource'
splineSource1 = SplineSource(registrationName='SplineSource1')
splineSource1.ParametricFunction = 'Spline'

# show data in view
splineSource1Display = Show(splineSource1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
splineSource1Display.Representation = 'Surface'
splineSource1Display.ColorArrayName = [None, '']
splineSource1Display.SelectTCoordArray = 'None'
splineSource1Display.SelectNormalArray = 'None'
splineSource1Display.SelectTangentArray = 'None'
splineSource1Display.OSPRayScaleFunction = 'PiecewiseFunction'
splineSource1Display.SelectOrientationVectors = 'None'
splineSource1Display.ScaleFactor = 0.1
splineSource1Display.SelectScaleArray = 'None'
splineSource1Display.GlyphType = 'Arrow'
splineSource1Display.GlyphTableIndexArray = 'None'
splineSource1Display.GaussianRadius = 0.005
splineSource1Display.SetScaleArray = [None, '']
splineSource1Display.ScaleTransferFunction = 'PiecewiseFunction'
splineSource1Display.OpacityArray = [None, '']
splineSource1Display.OpacityTransferFunction = 'PiecewiseFunction'
splineSource1Display.DataAxesGrid = 'GridAxesRepresentation'
splineSource1Display.PolarAxes = 'PolarAxesRepresentation'

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on splineSource1.ParametricFunction
points =[4152312.1574991588, 128917.82478350455, 0.0, 4152152.895532574, 130550.50404353943, 0.0, 4153089.995398994, 134268.8266573188, 0.0, 4154403.5219919425, 137703.76371706522, 0.0, 4154301.0425677244, 139369.86148628723, 0.0, 4155253.3113381774, 141244.96188753162, 0.0, 4155423.433954163, 142045.98641340825, 0.0, 4155131.616560585, 143965.47086945942, 0.0, 4154229.31076859, 146476.4904676368, 0.0, 4154126.1948228814, 147784.10115496867, 0.0, 4154890.09912743, 150460.86260358008, 0.0, 4155084.042516986, 152801.2353916032, 0.0, 4154749.862960395, 154615.35735550907, 0.0, 4154731.6585529167, 156239.13040415803, 0.0, 4155451.2536875396, 157713.9806395484, 0.0, 4155855.6599643016, 159822.01677370706, 0.0, 4156258.493658558, 161044.378940843, 0.0, 4157441.8634823356, 162434.05554091872, 0.0, 4158583.357894827, 163992.50682911804, 0.0, 4159303.215126534, 165614.96939234552, 0.0, 4158883.0007584933, 166480.3047327752, 0.0, 4158336.5610775454, 167514.564531091, 0.0, 4158358.884153491, 168210.4137770254, 0.0, 4158803.031622424, 168947.68912495812, 0.0]

reversed_points = []
for i in range(len(points) - 3, -1, -3):
    reversed_points.extend(points[i:i + 3])

splineSource1.ParametricFunction.Points = reversed_points

# update the view to ensure updated data information
renderView1.Update()

# find source
stClair = FindSource('StClair*')

# find source
splineSource1 = FindSource('SplineSource1')

# create a new 'Resample With Dataset'
resampleWithDataset1 = ResampleWithDataset(registrationName='ResampleWithDataset1', SourceDataArrays=stClair,
    DestinationMesh=splineSource1)
resampleWithDataset1.CellLocator = 'Static Cell Locator'

# create a new 'Plot Data'
plotData1 = PlotData(registrationName='PlotData1', Input=resampleWithDataset1)

# get active view
lineChartView1 = GetActiveViewOrCreate('XYChartView')

# show data in view
plotData1Display = Show(plotData1, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotData1Display.CompositeDataSetIndex = [0]
plotData1Display.XArrayName = 'Anchor Ice Thickness'
plotData1Display.SeriesVisibility = ['Anchor Ice Thickness', 'Bed Elev.', 'Border Ice Index', 'Bottom of Ice', 'Frazil Conc.', 'Frazil Ice Thickness', 'Froude Number', 'Ice Concentration', 'Ice Thickness', 'Ice Type', 'Ice Vel. Mag.', 'Ice Velocity Ui', 'Node #', 'Solid Crust Thickness', 'Surface Ice Thickness', 'Surface Water Temp.', 'Top of Ice', 'Undercover Ice Thickness', 'Vi', 'Vw', 'W.S.Elev.', 'Water Depth', 'Water Temperature', 'Water Vel. Mag.', 'Water Vel. Uw', 'Ww[=0]']
plotData1Display.SeriesLabel = ['Anchor Ice Thickness', 'Anchor Ice Thickness', 'Bed Elev.', 'Bed Elev.', 'Border Ice Index', 'Border Ice Index', 'Bottom of Ice', 'Bottom of Ice', 'Frazil Conc.', 'Frazil Conc.', 'Frazil Ice Thickness', 'Frazil Ice Thickness', 'Froude Number', 'Froude Number', 'Ice Concentration', 'Ice Concentration', 'Ice Thickness', 'Ice Thickness', 'Ice Type', 'Ice Type', 'Ice Vel. Mag.', 'Ice Vel. Mag.', 'Ice Velocity Ui', 'Ice Velocity Ui', 'Node #', 'Node #', 'Solid Crust Thickness', 'Solid Crust Thickness', 'Surface Ice Thickness', 'Surface Ice Thickness', 'Surface Water Temp.', 'Surface Water Temp.', 'Top of Ice', 'Top of Ice', 'Undercover Ice Thickness', 'Undercover Ice Thickness', 'Vi', 'Vi', 'vtkValidPointMask', 'vtkValidPointMask', 'Vw', 'Vw', 'W.S.Elev.', 'W.S.Elev.', 'Water Depth', 'Water Depth', 'Water Temperature', 'Water Temperature', 'Water Vel. Mag.', 'Water Vel. Mag.', 'Water Vel. Uw', 'Water Vel. Uw', 'Ww[=0]', 'Ww[=0]', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotData1Display.SeriesColor = ['Anchor Ice Thickness', '0', '0', '0', 'Bed Elev.', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Border Ice Index', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Bottom of Ice', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Frazil Conc.', '0.6', '0.3100022888532845', '0.6399938963912413', 'Frazil Ice Thickness', '1', '0.5000076295109483', '0', 'Froude Number', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Ice Concentration', '0', '0', '0', 'Ice Thickness', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Ice Type', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Ice Vel. Mag.', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Ice Velocity Ui', '0.6', '0.3100022888532845', '0.6399938963912413', 'Node #', '1', '0.5000076295109483', '0', 'Solid Crust Thickness', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Surface Ice Thickness', '0', '0', '0', 'Surface Water Temp.', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Top of Ice', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Undercover Ice Thickness', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Vi', '0.6', '0.3100022888532845', '0.6399938963912413', 'vtkValidPointMask', '1', '0.5000076295109483', '0', 'Vw', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'W.S.Elev.', '0', '0', '0', 'Water Depth', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Water Temperature', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Water Vel. Mag.', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Water Vel. Uw', '0.6', '0.3100022888532845', '0.6399938963912413', 'Ww[=0]', '1', '0.5000076295109483', '0', 'Points_X', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Y', '0', '0', '0', 'Points_Z', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Magnitude', '0.220004577706569', '0.4899977111467155', '0.7199969481956207']
plotData1Display.SeriesPlotCorner = ['Anchor Ice Thickness', '0', 'Bed Elev.', '0', 'Border Ice Index', '0', 'Bottom of Ice', '0', 'Frazil Conc.', '0', 'Frazil Ice Thickness', '0', 'Froude Number', '0', 'Ice Concentration', '0', 'Ice Thickness', '0', 'Ice Type', '0', 'Ice Vel. Mag.', '0', 'Ice Velocity Ui', '0', 'Node #', '0', 'Solid Crust Thickness', '0', 'Surface Ice Thickness', '0', 'Surface Water Temp.', '0', 'Top of Ice', '0', 'Undercover Ice Thickness', '0', 'Vi', '0', 'vtkValidPointMask', '0', 'Vw', '0', 'W.S.Elev.', '0', 'Water Depth', '0', 'Water Temperature', '0', 'Water Vel. Mag.', '0', 'Water Vel. Uw', '0', 'Ww[=0]', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotData1Display.SeriesLabelPrefix = ''
plotData1Display.SeriesLineStyle = ['Anchor Ice Thickness', '1', 'Bed Elev.', '1', 'Border Ice Index', '1', 'Bottom of Ice', '1', 'Frazil Conc.', '1', 'Frazil Ice Thickness', '1', 'Froude Number', '1', 'Ice Concentration', '1', 'Ice Thickness', '1', 'Ice Type', '1', 'Ice Vel. Mag.', '1', 'Ice Velocity Ui', '1', 'Node #', '1', 'Solid Crust Thickness', '1', 'Surface Ice Thickness', '1', 'Surface Water Temp.', '1', 'Top of Ice', '1', 'Undercover Ice Thickness', '1', 'Vi', '1', 'vtkValidPointMask', '1', 'Vw', '1', 'W.S.Elev.', '1', 'Water Depth', '1', 'Water Temperature', '1', 'Water Vel. Mag.', '1', 'Water Vel. Uw', '1', 'Ww[=0]', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotData1Display.SeriesLineThickness = ['Anchor Ice Thickness', '2', 'Bed Elev.', '2', 'Border Ice Index', '2', 'Bottom of Ice', '2', 'Frazil Conc.', '2', 'Frazil Ice Thickness', '2', 'Froude Number', '2', 'Ice Concentration', '2', 'Ice Thickness', '2', 'Ice Type', '2', 'Ice Vel. Mag.', '2', 'Ice Velocity Ui', '2', 'Node #', '2', 'Solid Crust Thickness', '2', 'Surface Ice Thickness', '2', 'Surface Water Temp.', '2', 'Top of Ice', '2', 'Undercover Ice Thickness', '2', 'Vi', '2', 'vtkValidPointMask', '2', 'Vw', '2', 'W.S.Elev.', '2', 'Water Depth', '2', 'Water Temperature', '2', 'Water Vel. Mag.', '2', 'Water Vel. Uw', '2', 'Ww[=0]', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotData1Display.SeriesMarkerStyle = ['Anchor Ice Thickness', '0', 'Bed Elev.', '0', 'Border Ice Index', '0', 'Bottom of Ice', '0', 'Frazil Conc.', '0', 'Frazil Ice Thickness', '0', 'Froude Number', '0', 'Ice Concentration', '0', 'Ice Thickness', '0', 'Ice Type', '0', 'Ice Vel. Mag.', '0', 'Ice Velocity Ui', '0', 'Node #', '0', 'Solid Crust Thickness', '0', 'Surface Ice Thickness', '0', 'Surface Water Temp.', '0', 'Top of Ice', '0', 'Undercover Ice Thickness', '0', 'Vi', '0', 'vtkValidPointMask', '0', 'Vw', '0', 'W.S.Elev.', '0', 'Water Depth', '0', 'Water Temperature', '0', 'Water Vel. Mag.', '0', 'Water Vel. Uw', '0', 'Ww[=0]', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotData1Display.SeriesMarkerSize = ['Anchor Ice Thickness', '4', 'Bed Elev.', '4', 'Border Ice Index', '4', 'Bottom of Ice', '4', 'Frazil Conc.', '4', 'Frazil Ice Thickness', '4', 'Froude Number', '4', 'Ice Concentration', '4', 'Ice Thickness', '4', 'Ice Type', '4', 'Ice Vel. Mag.', '4', 'Ice Velocity Ui', '4', 'Node #', '4', 'Solid Crust Thickness', '4', 'Surface Ice Thickness', '4', 'Surface Water Temp.', '4', 'Top of Ice', '4', 'Undercover Ice Thickness', '4', 'Vi', '4', 'vtkValidPointMask', '4', 'Vw', '4', 'W.S.Elev.', '4', 'Water Depth', '4', 'Water Temperature', '4', 'Water Vel. Mag.', '4', 'Water Vel. Uw', '4', 'Ww[=0]', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# update the view to ensure updated data information
lineChartView1.Update()

# Properties modified on plotData1Display
plotData1Display.SeriesPlotCorner = ['Anchor Ice Thickness', '0', 'Bed Elev.', '0', 'Border Ice Index', '0', 'Bottom of Ice', '0', 'Frazil Conc.', '0', 'Frazil Ice Thickness', '0', 'Froude Number', '0', 'Ice Concentration', '0', 'Ice Thickness', '0', 'Ice Type', '0', 'Ice Vel. Mag.', '0', 'Ice Velocity Ui', '0', 'Node #', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Solid Crust Thickness', '0', 'Surface Ice Thickness', '0', 'Surface Water Temp.', '0', 'Top of Ice', '0', 'Undercover Ice Thickness', '0', 'Vi', '0', 'Vw', '0', 'W.S.Elev.', '0', 'Water Depth', '0', 'Water Temperature', '0', 'Water Vel. Mag.', '0', 'Water Vel. Uw', '0', 'Ww[=0]', '0', 'vtkValidPointMask', '0']
plotData1Display.SeriesLineStyle = ['Anchor Ice Thickness', '1', 'Bed Elev.', '1', 'Border Ice Index', '1', 'Bottom of Ice', '1', 'Frazil Conc.', '1', 'Frazil Ice Thickness', '1', 'Froude Number', '1', 'Ice Concentration', '1', 'Ice Thickness', '1', 'Ice Type', '1', 'Ice Vel. Mag.', '1', 'Ice Velocity Ui', '1', 'Node #', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Solid Crust Thickness', '1', 'Surface Ice Thickness', '1', 'Surface Water Temp.', '1', 'Top of Ice', '1', 'Undercover Ice Thickness', '1', 'Vi', '1', 'Vw', '1', 'W.S.Elev.', '1', 'Water Depth', '1', 'Water Temperature', '1', 'Water Vel. Mag.', '1', 'Water Vel. Uw', '1', 'Ww[=0]', '1', 'vtkValidPointMask', '1']
plotData1Display.SeriesLineThickness = ['Anchor Ice Thickness', '2', 'Bed Elev.', '2', 'Border Ice Index', '2', 'Bottom of Ice', '2', 'Frazil Conc.', '2', 'Frazil Ice Thickness', '2', 'Froude Number', '2', 'Ice Concentration', '2', 'Ice Thickness', '2', 'Ice Type', '2', 'Ice Vel. Mag.', '2', 'Ice Velocity Ui', '2', 'Node #', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Solid Crust Thickness', '2', 'Surface Ice Thickness', '2', 'Surface Water Temp.', '2', 'Top of Ice', '2', 'Undercover Ice Thickness', '2', 'Vi', '2', 'Vw', '2', 'W.S.Elev.', '2', 'Water Depth', '2', 'Water Temperature', '2', 'Water Vel. Mag.', '2', 'Water Vel. Uw', '2', 'Ww[=0]', '2', 'vtkValidPointMask', '2']
plotData1Display.SeriesMarkerStyle = ['Anchor Ice Thickness', '0', 'Bed Elev.', '0', 'Border Ice Index', '0', 'Bottom of Ice', '0', 'Frazil Conc.', '0', 'Frazil Ice Thickness', '0', 'Froude Number', '0', 'Ice Concentration', '0', 'Ice Thickness', '0', 'Ice Type', '0', 'Ice Vel. Mag.', '0', 'Ice Velocity Ui', '0', 'Node #', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Solid Crust Thickness', '0', 'Surface Ice Thickness', '0', 'Surface Water Temp.', '0', 'Top of Ice', '0', 'Undercover Ice Thickness', '0', 'Vi', '0', 'Vw', '0', 'W.S.Elev.', '0', 'Water Depth', '0', 'Water Temperature', '0', 'Water Vel. Mag.', '0', 'Water Vel. Uw', '0', 'Ww[=0]', '0', 'vtkValidPointMask', '0']
plotData1Display.SeriesMarkerSize = ['Anchor Ice Thickness', '4', 'Bed Elev.', '4', 'Border Ice Index', '4', 'Bottom of Ice', '4', 'Frazil Conc.', '4', 'Frazil Ice Thickness', '4', 'Froude Number', '4', 'Ice Concentration', '4', 'Ice Thickness', '4', 'Ice Type', '4', 'Ice Vel. Mag.', '4', 'Ice Velocity Ui', '4', 'Node #', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Solid Crust Thickness', '4', 'Surface Ice Thickness', '4', 'Surface Water Temp.', '4', 'Top of Ice', '4', 'Undercover Ice Thickness', '4', 'Vi', '4', 'Vw', '4', 'W.S.Elev.', '4', 'Water Depth', '4', 'Water Temperature', '4', 'Water Vel. Mag.', '4', 'Water Vel. Uw', '4', 'Ww[=0]', '4', 'vtkValidPointMask', '4']

# Properties modified on plotData1Display
plotData1Display.SeriesVisibility = ['Anchor Ice Thickness', 'Bed Elev.', 'Border Ice Index', 'Bottom of Ice', 'Frazil Conc.', 'Frazil Ice Thickness', 'Froude Number', 'Ice Concentration', 'Ice Thickness', 'Ice Type', 'Ice Vel. Mag.', 'Ice Velocity Ui', 'Node #', 'Points_Magnitude', 'Points_X', 'Points_Y', 'Points_Z', 'Solid Crust Thickness', 'Surface Ice Thickness', 'Surface Water Temp.', 'Top of Ice', 'Undercover Ice Thickness', 'Vi', 'vtkValidPointMask', 'Vw', 'W.S.Elev.', 'Water Depth', 'Water Temperature', 'Water Vel. Mag.', 'Water Vel. Uw', 'Ww[=0]']

# get animation scene
animationScene1 = GetAnimationScene()

animationScene1.GoToLast()

# export view
ExportView(os.path.join(current_directory, 'post_process/centerline_output.csv'), view=lineChartView1, RealNumberNotation='Fixed')

# Properties modified on plotData1Display
plotData1Display.SeriesVisibility = []

# Properties modified on plotData1Display
plotData1Display.SeriesVisibility = ['W.S.Elev.']

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1045, 689)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [4163571.949919704, 164774.43201961194, 9999.999999999995]
renderView1.CameraFocalPoint = [4163571.949919704, 164774.43201961194, 0.0]
renderView1.CameraViewUp = [0.0017755744047769993, 0.9999984236665241, 0.0]
renderView1.CameraParallelScale = 7981.622022605196

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).