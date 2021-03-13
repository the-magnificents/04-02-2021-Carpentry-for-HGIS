# Exercise 1: Running someone else's Python script

QGIS is an open-source program that is written in Python, which makes it easy to interact with programmatically. You can use Python scripts for analysing data, create your own processing algorithms, and even change things about the appearance and functionality of your own version of the application.

Since a key function of scripts is reproducibility, people working with code often send and receive snippets or scripts from others that are written to accomplish a certain result. In QGIS it is no different - using the Code Editor, you can open a script someone else has written and run it to acheive the same result on your own.

We are going to use a script called gis_button.py that comes from the PyQGIS In A Day course [here](https://courses.spatialthoughts.com/pyqgis-in-a-day.html#add-a-new-menu-item). This script will add a new item to your Help menu in QGIS - a direct hyperlink to the [GIS StackExchange community forum](https://gis.stackexchange.com/) which has questions and answers to many common questions about working with GIS!
```{admonition} Exercise: Run the gis_button.py script
Open up the `pre_workshop_files/' folder and find the `qgis/` subfolder. It contains two scripts,airport_codes.py which we created in the demonstration, and gis_button.py which you can now try using on your own. 

In QGIS, open up the Python Code Editor and select the folder icon to \"Open Script\". Navigate to the gis_button.py script and click it so it loads into your Code Editor. Before you run anything, take a look at your \"help\" menu on the top of the screen so you can see the change that occurs when you run the script.

Remember how to run the script? What happens when you do?
```

:::{admonition} See Solution
:class: tip, dropdown
To run the gis_button.py script from the Code Editor, hit the \"play\" button. If you check out your Help menu now, you should see a link to the GIS StackExchange community that you can follow!
:::