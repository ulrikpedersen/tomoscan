Running a scan
==================

* Start the interactive bluesky environment. This is best done within the same network as the docker-compose environment which can be achieved by running: :code:`docker run --net tomoscan_default -it tomoscan`
* Start the phoebus screen to monitor the scan's progress. Navigate to the display folder and run :code:`./startOvervirew.sh`

There are two scan modes which are explained below. Outputs from the scan are saved to the data directory.

Synced scan
-------------
In the default setup the pulse generator triggers the laser IOC and then when running the synced scan the motor moves to its next position, waits for the laser PV to
go high and then bluesky triggers the areadetector. The motor then proceeds to its next positon. If implementing in hardware the idea would be that the pulse generator would trigger a laser as well as a "laser" PV and a delay wouldbe tuned to trigger the areadetecor at the correct time.

A synced scan between position -10 and 10 in 21 steps is run as:

.. code-block:: python

    RE(pulse_sync([det], motor1, laser1, -10, 10, 21))

Passive scan
-------------
For a passive scan the pulse generator is setup to directly trigger the areadetector. To enter this configuration you must uncomment the commented out camA section in pulse-id-gen.ini 
The Bluesky scan moves the motor and then waits for the detector to take an image before the motor moves again. Due to the detector not being directly triggered by Bluesky additional frames may sometimes by captured. The correct frames will be identifiable by the pulse IDs recorded by the Bluesky scan when compared with the pulse ID of the NDAttributes associated with the captured frame in the hdf5 file. 

A passive scan between position -20 and 20 in 11 steps is run as:

.. code-block:: python

    RE(passive_scan([det], motor1, -20, 20, 11, adStatus , pulse_ID))
