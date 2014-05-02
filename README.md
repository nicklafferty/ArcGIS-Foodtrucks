ArcGIS-Foodtrucks
=================

Python script that iterates over a list to add foodtrucks to a map of Dallas county

### About
This script reads Lat, Long coordinates from a text file and then projects them as point features into Arc Map and buffers 1 mile around them. A base map with street view of Dallas county is provided.

### Instructions

1. Clone to desktop
2. Copy the file path of the folder to your clip board
3. Open Terminal
4. Navigate to foodtrucks.py folder
5. Run the script with no arguments
6. The script will prompt you for a workspace, paste the file path you copied.
7. The script will ask for an author and title for the map
8. The script will save the file as "Foodtruck_copy.mxd"

### Final Note
Occasionally the foodtruck.shp file is created but contains no point data. This is a bug that I have not been able to fix. If this happens, please delete buffer.shp and foodtrucks.shp and run the script again. 