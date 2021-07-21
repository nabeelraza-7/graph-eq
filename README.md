# graph-eq
Graph plotter utility which allows users to plot handwritten expressions. 

# Configurations

clone this repo in your local directory by using:

    git clone https://github.com/nabeelraza-7/graph-eq/
  
Then go into the project root directory and enable python's environment. Recommended way is to use `pipenv` as follows, but users can also use `venv`

    pipenv shell

To install all the required libraries:

    pipenv install -r requirements.txt 

make sure you are in the same folder as `requirements.txt`

after that, cd into the grapheq library.

    cd grapheq
   
from there, run:

    python manage.py runserver

This should run the server on localhost if all the required libraries are installed and you have python in your `PATH` environment variable.
