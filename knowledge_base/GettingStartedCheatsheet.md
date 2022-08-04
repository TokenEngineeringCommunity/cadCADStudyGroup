### GettingStarted Cheatsheet 

### Installation
We'll be using python

Python 3.10.xx

#### Installation
 https://www.python.org/downloads/release/python-3105/

### Creating environments

#### venv
Typically we'll create virtual environments for our projects using venv
```
python3.10 -m venv venv
source ~/venv/venv/activate
```
This allows you to install things locally without interacting with the global space of the packages that you install

#### requirements.txt
It's useful to be able to just install a version of the packages used, we'll typically using requirements.txt to install necessary packages
```
# Generate a requirements.txt via pip freeze
pip freeze > requirements.txt
```

### Types
Types are awesome, in the future [cadcad](https://cadcad.org), datascience aligned projects will use types, we'll try and use types as well
so a good primer here is just the actual type systems documentation. Here's also a motivational [piece](https://hackernoon.com/type-annotation-in-python) thats good as well.

### Numpy
We'll probably using [numpy](https://numpy.org/) in some way or form. Numpy is a python package that makes it easier to perform 
math operations on vectors/matricies/list of data. 

### Matplotlib or Plotly
Both are great options, modellers choice. 
The text uses an outdated version of [matplotlib](https://matplotlib.org/)

### Jupyter Notebook
For this study group we have a great getting started [notebook](../templates/python/simple.ipynb)
and also a way to start evolving our setup with [notebook](../templates/cadcad_tools/mpp_example.ipynb) cribbed from 
the [cadcad tools repo](https://github.com/cadCAD-org/cadCAD-tools).

### Useful Python Topics
[List Comprehensios](https://www.learnpython.org/en/List_Comprehensions)
[Lambda Functions](https://www.learnpython.org/en/Lambda_functions)
[Type Annotations](https://docs.python.org/3/library/typing.html)
[Data Class](https://realpython.com/python-data-classes/#basic-data-classes)


