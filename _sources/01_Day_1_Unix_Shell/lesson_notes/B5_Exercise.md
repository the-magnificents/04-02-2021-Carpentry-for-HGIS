---
title: "Libraries"
teaching: 10
exercises: 10
questions:
- "How can I use software that other people have written?"
- "How can I find out what that software does?"
objectives:
- "Explain what software libraries are and why programmers create and use them."
- "Write programs that import and use modules from Python's standard library."
- "Find and read documentation for the standard library interactively (in the interpreter) and online."
keypoints:
- "Most of the power of a programming language is in its libraries."
- "A program must import a library module in order to use it."
- "Use `help` to learn about the contents of a library module."
- "Import specific items from a library to shorten programs."
- "Create an alias for a library when importing it to shorten programs."
---

> ## Jigsaw Puzzle (Parson's Problem) Programming Example
>
> Rearrange the following statements so that a random
> DNA base is printed and its index in the string.  Not all statements may be needed.  Feel free to use/add
> intermediate variables.
>
> ~~~
> bases="ACTTGCTTGAC"
> import math
> import random
> ___ = random.randrange(n_bases)
> ___ = len(bases)
> print("random base ", bases[___], "base index", ___)
> ~~~
> {: .language-python}
>
> > ## Solution
> >
> > ~~~
> > import math 
> > import random
> > bases = "ACTTGCTTGAC" 
> > n_bases = len(bases)
> > idx = random.randrange(n_bases)
> > print("random base", bases[idx], "base index", idx)
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

> ## When Is Help Available?
>
> When a colleague of yours types `help(math)`,
> Python reports an error:
>
> ~~~
> NameError: name 'math' is not defined
> ~~~
> {: .error}
>
> What has your colleague forgotten to do?
>
> > ## Solution
> >
> > Importing the math module (`import math`)
> {: .solution}
{: .challenge}

> ## Importing With Aliases
>
> 1. Fill in the blanks so that the program below prints `90.0`.
> 2. Rewrite the program so that it uses `import` *without* `as`.
> 3. Which form do you find easier to read?
>
> ~~~
> import math as m
> angle = ____.degrees(____.pi / 2)
> print(____)
> ~~~
> {: .language-python}
>
> > ## Solution
> >
> > ~~~
> > import math as m
> > angle = m.degrees(m.pi / 2)
> > print(angle)
> > ~~~
> > {: .language-python}
> >
> > can be written as
> >
> > ~~~
> > import math
> > angle = math.degrees(math.pi / 2)
> > print(angle)
> > ~~~
> > {: .language-python}
> >
> > Since you just wrote the code and are familiar with it, you might actually
> > find the first version easier to read. But when trying to read a huge piece
> > of code written by someone else, or when getting back to your own huge piece
> > of code after several months, non-abbreviated names are often easier, except
> > where there are clear abbreviation conventions.
> {: .solution}
{: .challenge}

> ## There Are Many Ways To Import Libraries!
>
> Match the following print statements with the appropriate library calls.
>
> Print commands:
>
> 1. `print("sin(pi/2) =", sin(pi/2))`
> 2. `print("sin(pi/2) =", m.sin(m.pi/2))`
> 3. `print("sin(pi/2) =", math.sin(math.pi/2))`
>
> Library calls:
>
> 1. `from math import sin, pi`
> 2. `import math`
> 3. `import math as m`
> 4. `from math import *`
>
> > ## Solution
> >
> > 1. Library calls 1 and 4. In order to directly refer to `sin` and `pi` without
> >    the library name as prefix, you need to use the `from ... import ...`
> >    statement. Whereas library call 1 specifically imports the two functions
> >    `sin` and `pi`, library call 4 imports all functions in the `math` module.
> > 2. Library call 3. Here `sin` and `pi` are referred to with a shortened library
> >    name `m` instead of `math`. Library call 3 does exactly that using the
> >    `import ... as ...` syntax - it creates an alias for `math` in the form of
> >    the shortened name `m`.
> > 3. Library call 2. Here `sin` and `pi` are referred to with the regular library
> >    name `math`, so the regular `import ...` call suffices.
> {: .solution}
{: .challenge}

> ## Importing Specific Items
>
> 1. Fill in the blanks so that the program below prints `90.0`.
> 2. Do you find this version easier to read than preceding ones?
> 3. Why *wouldn't* programmers always use this form of `import`?
>
> ~~~
> ____ math import ____, ____
> angle = degrees(pi / 2)
> print(angle)
> ~~~
> {: .language-python}
>
> > ## Solution
> >
> > ~~~
> > from math import degrees, pi
> > angle = degrees(pi / 2)
> > print(angle)
> > ~~~
> > {: .language-python}
> >
> > Most likely you find this version easier to read since it's less dense.
> > The main reason not to use this form of import is to avoid name clashes.
> > For instance, you wouldn't import `degrees` this way if you also wanted to
> > use the name `degrees` for a variable or function of your own. Or if you
> > were to also import a function named `degrees` from another library.
> {: .solution}
{: .challenge}

> ## Reading Error Messages
>
> 1. Read the code below and try to identify what the errors are without running it.
> 2. Run the code, and read the error message. What type of error is it?
>
> ~~~
> from math import log
> log(0)
> ~~~
> {: .language-python}
>
> > ## Solution
> >
> > 1. The logarithm of `x` is only defined for `x > 0`, so 0 is outside the
> >    domain of the function.
> > 2. You get an error of type "ValueError", indicating that the function
> >    received an inappropriate argument value. The additional message
> >    "math domain error" makes it clearer what the problem is.
> {: .solution}
{: .challenge}

[pypi]: https://pypi.python.org/pypi/
[stdlib]: https://docs.python.org/3/library/
[randommod]: https://docs.python.org/3/library/random.html
