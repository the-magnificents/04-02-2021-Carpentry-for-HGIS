# Exercise 1

### Select and concatenate data files

In Bash, `*` is a wildcard, which matches zero or more characters. When the shell sees a wildcard, it expands the wildcard to create a list of matching filenames before running the command that was asked for. As an exception, if a wildcard expression does not match any file, Bash will pass the expression as an argument to the command as it is. For example typing `ls *.pdf` in the `cities_data/` directory (which does not contains any pdf files) results in an error message that there is no file called `*.pdf`. 

Here's how the wildcard works in practice: `*.csv` matches amsterdam-nl.csv, eindhoven-nl.csv and every file that ends with ‘.csv’. On the other hand, `n*.csv` only matches newyorkcity-us.csv because the ‘n’ at the front only matches filenames that begin with the letter ‘n’.

```{admonition} Exercise: Explore data files
 Take a look at the contents of the `cities_data/` directory. Use `ls` and `cat` to inspect the names, file extensions and contents of the files. What patterns and information do you see? **Tip:** you can write your observations in comments section of the workshop website, and see what others observed! :) 
```

:::{admonition} See Solution
:class: tip, dropdown
The names of all the .csv and text files in the `cities_data/` directory follow a standard pattern, `cityname-countrycode.csv` or `cityname-countrycode.txt`. This is good practice when working with Bash - it is much easier to ask the computer to find and do something with files that match a convention in their names. You'll also see that there are no spaces in any filenames, and no capital letters. Instead, we see a lot of dashes.

We have three types of data files in the `cities_data/` directory: .txt, .csv, and .md. The only .md file is called README.md, and contains some very brief information about the data and the imaginary project they were collected for. It is good practice as well to include a README.md file with any code or data project, and to fill it (much better than we did here) with documentation that can help you or someone else replicate the data and/or the results of your research. 
:::

```{admonition} Exercise: Select and concatenate data files
 Right now, the data for each city in the `cities_data/` folder are each stored in separate files per city. That might be helpful for some applications, but we want a list of data in one .csv file. How could we do that?
```

:::{admonition} See Solution
:class: tip, dropdown
We can use the wildcard `*` to grab all the .csv files this time in the `cities_data` folder. We want to concatenate all files related to cities in the Netherlands, so we should use `*-nl.csv` to match all the files from the Netherlands in the directory. We use the `awk` command (used for pattern scanning and processing) along with the 1 flag which automatically inserts a new line between the data from each of the separate files. The `>` symbol will concatenate the contents of all files that match this naming pattern to a new file that we define, in this case called netherlands-cities.csv.

`$ awk 1 *-nl.csv > netherlands-cities.csv`

You can use `ls` to see the files in the `cities_data/` folder, and `cat` to check out the contents of the newly created `netherlands-cities.csv`.
:::

```{admonition} Exercise: add data to netherlands-cities.csv
 Right now, the netherlands-cities.csv file contains geographic and population data for the 5 largest cities in the Netherlands (Amsterdam, Eindhoven, Rotterdam, The Hague and Utrecht). A good start, but there are many more places of interest in the Netherlands! Add a few more cities to the netherlands-cities.csv file using nano on the command line. Don't forget to keep the same format as the rest of the data: c,cityname,lat,lon,population. **Bonus:** add info about the source(s) of your population data by editing the README.md file.
```
:::{admonition} See Solution
:class: tip, dropdown
Use nano to open the netherlands-cities.csv file to add some data for other cities in the Netherlands. Make sure you start a new line for each city you add.

`$ nano netherlands-cities.csv`

Hit shift + control + O to "WriteOut" the file (save it). Nano will ask you if you want to save this file with the same name, and we do, so hit enter. You can then hit shift + control + X to exit the Nano text editor and get back to your bash shell.

You can do the same process to edit the README.md file: `nano README.md` will open the editor and allow you to insert information about the sources of your data.

If you now use cat to check out the contents of your file(s), you should see the changes you've made:

`$ cat netherlands-cities.csv` ; `cat README.md`
:::