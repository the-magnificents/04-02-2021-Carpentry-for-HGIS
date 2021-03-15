---
title: "Reading Tabular Data into DataFrames"
teaching: 10
exercises: 10
questions:
- "How can I read tabular data?"
objectives:
- "Import the Pandas library."
- "Use Pandas to load a simple CSV data set."
- "Get some basic information about a Pandas DataFrame."
keypoints:
- "Use the Pandas library to get basic statistics out of tabular data."
- "Use `index_col` to specify that a column's values should be used as row headings."
- "Use `DataFrame.info` to find out more about a dataframe."
- "The `DataFrame.columns` variable stores information about the dataframe's columns."
- "Use `DataFrame.T` to transpose a dataframe."
- "Use `DataFrame.describe` to get summary statistics about data."
---


> ## Reading Files in Other Directories
>
> The data for your current project is stored in a file called `microbes.csv`,
> which is located in a folder called `field_data`.
> You are doing analysis in a notebook called `analysis.ipynb`
> in a sibling folder called `thesis`:
>
> ~~~
> your_home_directory
> +-- field_data/
> |   +-- microbes.csv
> +-- thesis/
>     +-- analysis.ipynb
> ~~~
> {: .output}
>
> What value(s) should you pass to `read_csv` to read `microbes.csv` in `analysis.ipynb`?
> 
> > ## Solution
> > We need to specify the path to the file of interest in the call to `pd.read_csv`. We first need to 'jump' out of
> > the folder `thesis` using '../' and then into the folder `field_data` using 'field_data/'. Then we can specify the filename `microbes.csv.
> > The result is as follows:
> > ~~~
> > data_microbes = pd.read_csv('../field_data/microbes.csv')
> > ~~~
> >{: .language-python}
> {: .solution}
{: .challenge}

> ## Writing Data
> 
> As well as the `read_csv` function for reading data from a file,
> Pandas provides a `to_csv` function to write dataframes to files.
> Applying what you've learned about reading from files,
> write one of your dataframes to a file called `processed.csv`.
> You can use `help` to get information on how to use `to_csv`.
> > ## Solution
> > In order to write the DataFrame `americas` to a file called `processed.csv`, execute the following command:
> > ~~~
> > americas.to_csv('processed.csv')
> > ~~~
> >{: .language-python}
> > For help on `to_csv`, you could execute, for example,
> > ~~~
> > help(americas.to_csv)
> > ~~~
> >{: .language-python}
> > Note that `help(to_csv)` throws an error! This is a subtlety and is due to the fact that `to_csv` is NOT a function in 
> > and of itself and the actual call is `americas.to_csv`. 
> {: .solution}
{: .challenge}
