## Select and concatenate data files

The data we want to use are contained in multiple files located in the workshop_data/ folder that we sent out prior to this workshop. Let's take a look at the contents of that folder by navigating there in the shell. If you are in your `cities_data/` folder, you can use a special notation that means "move up one level": Right now, the data are each stored in separate files per city. That might be helpful for some applications, but we want a list of data in one .csv file. We can do this on the command line by using a combination of the `awk` command (used for pattern scanning and processing) and `>`, which concatenates the contents of multiple files to a new file that in this case we will call `netherlands-cities.csv`.

We can use the wildcard `*` to grab all the .csv files this time in the `cities_data` folder. We want to concatenate all files related to cities in the Netherlands, so we should use `*-nl.csv` to match all the files in that directory.

`$ awk 1 *-nl.csv > netherlands-cities.csv`

This will save a new file called `netherlands-cities.csv` in the `cities_data/` folder and automatically create a new line between each city. Check to see if it's there! You can use `ls` to see the files in the `data/` folder, and `cat` to check out the contents of the newly created `netherlands-cities.csv`.

`$ cd cities_data/`
`$ ls`
`$ cat netherlands-cities.csv`

## Add data to `netherlands-cities.csv`

We want to add more cities of interest. We can do this by editing the `netherlands-cities.csv` file we just created - you guessed it, using the command line!

Nano is a text editor that you can use direcly in your shell interface. There are a few of these, including vi and vim, but today we'll just work with nano. These should come with your shell so there's no need for a separate installation. To open a file with nano, use:

`$ nano <filename>`

Let's open the netherlands-cities.csv file to add some road data that we will specify now.

`$ nano netherlands-cities.csv`

Unlike using the `cat` command, nano opens the file contents in a new interface with a black bar at the top and some options at the bottom. Also new is that you can edit the contents of a file and save or 'write out' the file afterward. This is what we'll do now. Note that you can use your arrow keys to navigate the file to make changes, as clicking and inserting is not an option.

Add a few lines to the netherlands-cities.csv file:

c,cityname,____

Make sure there is a new line between each new city.

Now, press shift + control + O to "WriteOut" the file (save it). Nano will ask you if you want to save this file with the same name, and we do, so press enter. You can then press shift + control + X to exit the Nano text editor and get back to your bash shell.

If you now use cat to check out the contents of your file, you should see that it has been updated:

`$ cat netherlands-cities.csv`