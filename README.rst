===========================
tomoscan
===========================

|code_ci| |docs_ci| |coverage| |license|

.. note::

    This project is in very early development and intended for
    demonstration purposes only.

This project demonstrates the use of BlueSky to orchestrate a Tomography scan
for the new EPAC laser facility at Harwell Campus, UK.

============== ==============================================================
Source code    https://github.com/ulrikpedersen/tomoscan
Documentation  https://ulrikpedersen.github.io/tomoscan
Releases       https://github.com/ulrikpedersen/tomoscan/releases
============== ==============================================================



Some very brief examples of use:

.. code-block:: python

    from tomoscan import __version__

    print(f"Hello tomoscan {__version__}")

.. |code_ci| image:: https://github.com/ulrikpedersen/tomoscan/actions/workflows/code.yml/badge.svg?branch=main
    :target: https://github.com/ulrikpedersen/tomoscan/actions/workflows/code.yml
    :alt: Code CI

.. |docs_ci| image:: https://github.com/ulrikpedersen/tomoscan/actions/workflows/docs.yml/badge.svg?branch=main
    :target: https://github.com/ulrikpedersen/tomoscan/actions/workflows/docs.yml
    :alt: Docs CI

.. |coverage| image:: https://codecov.io/gh/ulrikpedersen/tomoscan/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/ulrikpedersen/tomoscan
    :alt: Test Coverage

.. |license| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
    :target: https://opensource.org/licenses/Apache-2.0
    :alt: Apache License


Download and install instructions
=================================

These instructions assume the use of Ubuntu 22.04. However, given that all code is run within Docker containers this system would be expected to run easily on other systems.

Prerequisites
----------------
* Docker is required to be installed on your PC. Instructions to install Docker Engine on Ubuntu can be found at https://docs.docker.com/engine/install/ubuntu/
* An installation of Phoebus is recommended to observe the scans. Phoebus can be downloaded from https://controlssoftware.sns.ornl.gov/css_phoebus/
* If using VSCode installing the H5Web extension allows the easy viewing of the hdf output files from scans
* To use EPAC Docker images from ghcr.io you need to ensure that you have an access token setup. This can be done by following the instructions `here <https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry#authenticating-with-a-personal-access-token-classic>`_

Setup
-------------
* Clone this repository using :code:`git clone git@github.com:ulrikpedersen/tomoscan.git`
* Build the top level bluesky environment Docker container by running :code:`docker build -t tomoscan .`
* Navigate to the sim folder and build the docker files for the simulation and IOCs by running :code:`./build.sh`

Running
=============

Synced scan
-------------

Passive scan
-------------


..
    Anything below this line is used when viewing README.rst and will be replaced
    when included in index.rst

See https://ulrikpedersen.github.io/tomoscan for more detailed documentation.
