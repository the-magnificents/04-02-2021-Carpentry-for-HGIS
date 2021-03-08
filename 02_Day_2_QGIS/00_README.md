# Working with the Python console in QGIS

From the QGIs documentation: "The QGIS Python Console is an interactive shell for the python command executions. It also has a python file editor that allows you to edit and save your python scripts." ([source](https://docs.qgis.org/2.18/en/docs/user_manual/plugins/python_console.html))

The console main features are:

- Code completion, highlighting syntax and calltips for the following APIs:
  - Python
  - PyQGIS
  - PyQt4
  - QScintilla2
  - osgeo-gdal-ogr
- Ctrl+Alt+Space to view the auto-completion list if enabled in the Options;
- Execute code snippets from the input area by typing and pressing Enter or Run Command;
- Execute code snippets from the output area using the Enter selected from the contextual menu or pressing Ctrl+E;
- Browse the command history from the input area using the Up and Down arrow keys and execute the command you want;
- Ctrl+Shift+Space to view the command history: double-clicking a row will execute the command. The Command History dialog can also be accessed from context menu of input area;
- Save and clear the command history. The history will be saved into the file ~/.qgis2/console_history.txt;
- Open QGIS API documentation by typing _api;
- Open PyQGIS Cookbook by typing _pyqgis

You can use the Python console to work programmatically with QGIS, which is especially useful if you want to perform the same processing action multiple times or over multiple files, and create documenatation for your analysis protocol which is an important part of a reproducible workflow. 

This lesson will demonstrate how to programmatically access the attribute of each feature of a dataset (the [International Airports dataset from Natural Earth](http://www.naturalearthdata.com/downloads/10m-cultural-vectors/airports/)), change the appearance of point data on a map, use the geometry function to access the coordinates of each feature in the dataset, and save a script that produces a .csv file with the name, iata code, latitude and longitude of every international airport in the world.

