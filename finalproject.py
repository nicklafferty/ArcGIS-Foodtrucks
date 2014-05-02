# Script Author: Nick Lafferty
# GISC 6317 - Fall 2013
'''Note:
The script begins by asking for a workspace.
Simply copy/paste the location of the 'final project' directory.
Everything else will just work.'''

import arcpy

# Ask user for workspace path
wkspace = raw_input("Please enter a workspace path. E.g. C:\Users\Desktop")
# Convert to string
strwkspace = str(wkspace)
# Set new workspace
arcpy.env.workspace = strwkspace
# Set the map document
mxd = arcpy.mapping.MapDocument("FoodTruck.mxd")
# Set infile
infile = strwkspace + "\\foodtrucks.txt"

# Set feature class name and spatial reference
fc = "foodtrucks.shp"
sr = arcpy.SpatialReference(4269)

# Create empty point feature class
arcpy.CreateFeatureclass_management(strwkspace, fc, "Point", "", "", "", sr)

# Insert Cursor
cursor = arcpy.da.InsertCursor(fc, ["SHAPE@"])

# Open text file
f = open(infile)

# Create array to store point coordinates
array = arcpy.Array()
point = arcpy.Point()

# Loop through the data
for line in f:
	point.X, point.Y = line.split()
	array.add(point)
	# Add array to the point object, insert point into cursor
	point1 = arcpy.PointGeometry(point)
	cursor.insertRow([point1])

# Close the text file and delete the cursor
f.close()
del cursor


# Map Script

# Set the author
author = raw_input("Who is the author for this map?")
mxd.author = author
# Set the title
title = raw_input("What is the title for this map?")
mxd.title = title
# Set the data frame
df = arcpy.mapping.ListDataFrames(mxd, "*")[0]
# Add food truck layer
truckspace = strwkspace + "\\foodtrucks.shp"
addLayer = arcpy.mapping.Layer(truckspace)
arcpy.mapping.AddLayer(df, addLayer, "TOP")
del addLayer


# Buffer Locations

# Set Buffer to workspace
buffspace = strwkspace + "\\buffer"
# Buffer Analysis
arcpy.Buffer_analysis("foodtrucks.shp", buffspace, "1 Miles")
# Set buff layer
buffLayer = strwkspace + "\\buffer.shp"
# Add buffer to map document
addLayer = arcpy.mapping.Layer(buffLayer)
# Auto arrange the buffer layer so it doesn't overlap the point data
arcpy.mapping.AddLayer(df, addLayer, "AUTO_ARRANGE")

# Set copy space
copyspace = strwkspace + "\\FoodTrucks_Copy.mxd"
mxd.saveACopy(copyspace)

del mxd