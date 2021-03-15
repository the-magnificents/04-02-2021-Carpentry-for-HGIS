# Programmatically access the attributes of international airports

This part of the lesson material is meant to be run as a demonstration, so there is no need to get ready with hands-on following along. However, if you are interested the data and scripts used in this lesson are in the 'qgis/' folder that was included in the 'pre_workshop_files/' folder.

1. Open QGIS and use the left side menu to navigate to Natural Earth datasets (airports and countries). Drag and drop both to the mapping view.
2. Use info button to show attributes of each airport (feature), pointing out name and iata_code as we will be saving those).
3. Open the Python console either from the plugins menu or the button on the header menu.
 
4. Save the airports dataset as a variable called layer: \n",

layer = iface.activeLayer()

5. Change the shape and color of the symbols representing airports:

symbol = QgsMarkerSymbol.createSimple({'name': 'cross', 'color': 'black'})
layer.renderer().setSymbol(symbol)
layer.triggerRepaint()

6. For loop that prints the name and iata_code for each airport on the list, using the function getFeatures that allows you to reference all features of a layer. In this case, the features are airports (point data). 

for f in layer.getFeatures():
  print(f"{f['name']}, {f['iata_code']}")

7. Access the coordinates of the feature (airport) using the geometry function. Returns a geometry object that we can store in a variable called geom. The asPoint() function gets the x and y coordinates of the point. 

for f in layer.getFeatures():
  geom = f.geometry()
  print(geom.asPoint())

8. Print the name, iata_code, lat and long of each of the airports. The .2f truncates lat and long to 2 decimal places:

for f in layer.getFeatures():
  geom = f.geometry()
  print(f"{f['name']}, {f['iata_code']}, ({geom.asPoint().y():.2f},{geom.asPoint().x():.2f})")

9. Store the output in a csv file instead of printing it in the console. To do this step on your own, need to replace your file path.

with open("/Users/acryan/Desktop/airports.csv","w") as output_file:
    for f in layer.getFeatures():
        geom = f.geometry()
        line = f"{f['name']},{f['iata_code']},{geom.asPoint().y():.2f},{geom.asPoint().x():.2f}\n"
        o=output_file.write(line)


At this point there should be a file called `airports.csv` on the Desktop. This file can be used as an input for a next analysis step or stored as supplementary material for a project or manuscript. It's a lot easier than copy and pasting that information from a database or website! :) 

## Saving a Python script for QGIS

Whenever possible, it's good practice to document exactly how you generated data. In this case you can do that by showing how you created the subset of data - since we used code, we can save it as a script that anyone else could use to produce the same results (the airports.csv file).

1. Open the Code Editor
2. Copy and paste the last command into the Code Editor
3. Save it as a script called airport_codes.py

Helpful links:
- https://docs.qgis.org/3.16/en/docs/user_manual/processing/scripts.html
- https://courses.spatialthoughts.com/pyqgis-in-a-day.html#where-can-you-use-python-in-qgis

