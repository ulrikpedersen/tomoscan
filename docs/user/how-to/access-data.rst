Accessing data
==================

Data from the scans is saved using the `Databroker <https://blueskyproject.io/databroker/>`_ to the mongoDB database which runs as part of the docker compose file.
The data from all scans run will remain available in the databroker catlog as long as the mongoDB docker container is running. 

Accessing a run
----------------
There are multiple ways of accessing a run from the databroker catalog. 

* The first is via a run's uid which is returned when the run is run. For example if running a run as :code:`uids = RE(pulse_sync([det], motor1, laser1, -10, 10, 11))` then the run can be accessed as :code:`run = catalog[uids[0]]`.

* Runs can also be accessed be their recency. To access the most recent run use :code:`run = catalog[-1]`, to access the second most recent run replace :code:`-1` with :code:`-2` and so on.

Run data
----------------
To access the run data as an `xarray dataset <https://docs.xarray.dev/en/stable/generated/xarray.Dataset.html>`_ use :code:`data = run.primary.read()`.
For the synced scan this data includes the laser pulse ID, the motor position and the image captured by the detector. 

Image access
_______________

The image data is accessed as :code:`image = data["det_image"]`. Individual frames are then accessed as :code:`frame = image[0][0]`.
The first index refers to the time of the image and the second index refers to the frame number of that detector triggering. 
If only capturing one frame per trigger then this second index will always be 0.

