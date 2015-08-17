Graph visualisation software for siyavula

This is currently a horizontal prototype and will achieve the following:
    1] Parse the data from a .map file
    2] create python objects from the data
    3] output a JSON file called data.json with the necessary node and edge information
    2] Start a server that will render a visualization of the nodes and edges on localhost:8000

To setup the environment to run the prototype

    1] ensure that python, virtualenv and python-pip package are installed/working on your machine 

    2]run the following:
        sudo sh bootsrap.sh

Then navigate to localhost:8000 on an internet browser

Use
    ctrl + c
to stop the server hosting the visualization

DISCLAIMER: This code has not been tested on a Windows Machine, only on OSX and Linux- Ubuntu. Please run this code on a unix machine.
For the above code to run, please ensure that virtualenv and the python-pip package are installed on your machine. They are not installed on the UCT Senior Lab computers and require permission from admin to be installed.

https://virtualenv.pypa.io/en/latest/
https://pypi.python.org/pypi/pip