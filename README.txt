Graph visualisation software for siyavula

This package will achieve the following:
    1] Parse the data from all .map files in the root folder
    2] create python objects from the data
    3] output a JSON file called data.json with the necessary node, edge and group information
    2] Start a server that will render a visualization of the nodes and edges on localhost:8000

To setup the environment to run the software

    1] ensure that python, virtualenv and python-pip package are installed/working on your machine 

    2]run the following:
        sudo sh bootsrap.sh

Then navigate to localhost:8000 on Chrome (it will not work on another browser)

to stop the server hosting the visualization, use:
    ctrl + c

To run the tests, run the following:
    sh test.sh

To run the tests with coverage reports:
    sh testcov.sh    

DISCLAIMER: This code has not been tested on a Windows Machine, only on OSX and Linux- Ubuntu. Please run this code on a unix machine.
For the above code to run, please ensure that virtualenv and the python-pip package are installed on your machine. They are not installed on the UCT Senior Lab computers and require permission from admin to be installed.

https://virtualenv.pypa.io/en/latest/
https://pypi.python.org/pypi/pip