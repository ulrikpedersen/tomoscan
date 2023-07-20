Installation
============

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

A .env file is used to supply information on the CLF docker containers used in the docker compose environment.
Copy the example-dotenv file to create a local .env file as follows:

::

    $ cp example-dotenv .env

Bring up the runtime environment
================================

The runtime environment consists of a number of services which can be brought up/down on a local development machine using docker compose.

.. _logging-service:

Start and access logging service
--------------------------------

The many services can log into a single location for easy searching and monitoring. A separate docker compose file named :code:`graylog-compose.yml` can be used to bring up a Graylog stack.

First configure a graylog admin account password:

::

    $ cat example-graylog-dotenv >> .env

Now edit the :code:`.env` file and fill in the :code:`GRAYLOG_ROOT_PASSWORD_SHA2` and :code:`GRAYLOG_PASSWORD_SECRET` as per the comments in the file. For example if choosing a strong password like 'mysupersecretpassword1234':

::

    $ pwgen -N 1 -s 96
    MXOuTyOQVxSmLL9lxGanDHyw8az3S7PkDmzlKFLfPH081xFgxmcMxwY3DsQxDN5cjfFGS01v7RtDVJRj9dxbGZht4IN992l6

Then set :code:`GRAYLOG_PASSWORD_SECRET=MXOuTyOQVxSmLL9lxGanDHyw8az3S7PkDmzlKFLfPH081xFgxmcMxwY3DsQxDN5cjfFGS01v7RtDVJRj9dxbGZht4IN992l6`

::

    $ echo -n mysupersecretpassword1234 | shasum -a 256
    3645ac65291ec7ec95d7d3697c9309b0edfbdbad7e904a39406a88a6b80bca28  -

Then set :code:`GRAYLOG_ROOT_PASSWORD_SHA2=3645ac65291ec7ec95d7d3697c9309b0edfbdbad7e904a39406a88a6b80bca28`

Now you can start the graylog services with docker compose:

::

    $ docker compose -f graylog-compose.yml up -d

Connect to the graylog web-interface on http://localhost:9000 and login with the :code:`admin` user and the password selected above. On the graylog web interface, navigate to "Search" (top left menu). Then select a time-window or "all messages" (top left clock) and click the green search button. Start the automatic updating and set the poll to "1 Second" (top right corner). Now you are ready to see logs when starting up the control system services in the next steps...

Start the Control System
------------------------

The simulation control system with motor, and areaDetector IOCs as well as laser pulse simulation can be started with docker compose:

::

    $ docker compose up -d

Logs from the services should be available on the :ref:`Graylog web interface<logging-service>`.

The services can be stopped/downed with docker compose:

::

    $ docker compose [stop|down] 

