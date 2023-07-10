Developer install
=================

These instructions assume the use of Ubuntu 22.04. However, given that all code is run within Docker containers this system would be expected to run easily on other systems.

Prerequisites
----------------
* Docker is required to be installed on your PC. Instructions to install Docker Engine on Ubuntu can be found at https://docs.docker.com/engine/install/ubuntu/
* An installation of Phoebus is recommended to observe the scans. Phoebus can be downloaded from https://controlssoftware.sns.ornl.gov/css_phoebus/
* If using VSCode installing the H5Web extension allows the easy viewing of the hdf output files from scans
* To use EPAC Docker images from ghcr.io you need to ensure that you have an access token setup. This can be done by following the instructions `here <https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry#authenticating-with-a-personal-access-token-classic>`_

Setup
-------------
Clone this repository using:

::

    $ git clone clone git@github.com:ulrikpedersen/tomoscan.git

Build the top level bluesky environment Docker container by running

::
    
    $ docker build -t tomoscan .

Navigate to the sim folder and build the docker files for the simulation and IOCs by running

::
    
    $ ./build.sh

It can be easier to make changes to the python script which launches bluesky :code:`src/ophyd_inter_setup.py` locally rather than in a Docker container during development. 
In that case use a python venv to install the dependencies of the python script as:

.. code::

            $ cd tomoscan
            $ python3 -m venv venv
            $ source venv/bin/activate
            $ pip install -e '.[dev]'
