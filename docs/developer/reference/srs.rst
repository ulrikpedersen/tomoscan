==================================
Software Requirement Specification
==================================

This is a requirements specification for a Tomography Scan demonstrator application for the STFC/CLF/EPAC laser facility.

Introduction
============

The `tomoscan` application will demonstrate the orchestration of a single-dimension scan of a sample in a Tomography laser experiment. While the project will deliver a real-time control system and demonstration of the tomography scan, the devices it controls are simulated.

Scope
-----

The project includes `EPICS`_ IOCs with simulated hardware: motor, shutter and detector as well as an installation of BlueSky and a suitable experiment plan for a tomography experiment.

The project does not include tomographic reconstruction of the acquired data.

Intended Audience
-----------------

Data Acquisition developers and scientists at EPAC.

Intended Use
------------

The use of this application is to evaluate the technology choices behind it: in particular the use of the Python and the `EPICS`_ `BlueSky`_ and `Ophyd`_ frameworks for the use-case of performing a Computed Tomography scan of a sample using a pulsed laser light source.

Functional requirements
=======================

The application `tomoscan` must perform a step-scan of a simulated motor, triggering and acquiring images from a simulated detector in synchronisation with simulated laser pulses.

External requirements
=====================

User interfaces
---------------

The user interface (UI) of `tomoscan` will primarily be an interactive python terminal and a         commandline (CLI) script, performing the BlueSky scan.

The Phoebus EPICS display manager (DM) will be used as a monitoring tool to view the simulation running.

Non-functional requirements
===========================

Runtime Environment
-------------------

The `tomoscan` application itself will only execute the scan itself.

EPICS control system IOCs will be included in the project to provide the simulated runtime environment.

EPICS simulations
-----------------

The simulated motor representation will be based on the EPICS motor record with a simulation backend.

The detector will be an EPICS areaDetector simulation using simDetector.

The laser pulse, shutter and ancillery parts of the Control System will be simulated using EPICS database logic and records.

.. _EPICS: https://epics-controls.org/
.. _BlueSky: https://blueskyproject.io/
.. _Ophyd: https://blueskyproject.io/ophyd/