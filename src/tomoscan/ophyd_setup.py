import time as ttime

import bluesky.plan_stubs as bps
from bluesky import RunEngine
from bluesky.callbacks.best_effort import BestEffortCallback
from bluesky.plan_stubs import mv
from bluesky.plans import count, scan  # noqa F401
from databroker import Broker
from ophyd import (
    ADComponent,
    AreaDetector,
    Component,
    Device,
    EpicsMotor,
    EpicsSignal,
    EpicsSignalRO,
    SingleTrigger,
)
from ophyd.areadetector import cam
from ophyd.areadetector.filestore_mixins import (
    FileStoreHDF5IterativeWrite,
    FileStoreTIFFIterativeWrite,
)
from ophyd.areadetector.plugins import HDF5Plugin_V34, TIFFPlugin_V34


class MyHDF5Plugin(FileStoreHDF5IterativeWrite, HDF5Plugin_V34):
    ...


class MyTIFFPlugin(FileStoreTIFFIterativeWrite, TIFFPlugin_V34):
    ...


class MyDetector(SingleTrigger, AreaDetector):
    cam = ADComponent(cam.AreaDetectorCam, "CAM:")
    hdf1 = ADComponent(
        MyHDF5Plugin,
        "HDF1:",
        write_path_template="/home/bar/BlueSkyTests/output/%Y/%m/%d",
    )
    tiff1 = ADComponent(
        MyTIFFPlugin,
        "TIFF1:",
        write_path_template="/home/bar/BlueSkyTests/output/%Y/%m/%d",
    )


class MyLaser(Device):
    power = Component(EpicsSignalRO, "power")
    pulse_id = Component(EpicsSignalRO, "pulse_id")
    pulse_time = Component(EpicsSignalRO, "pulse_time")
    freq = Component(EpicsSignalRO, "freq", kind="config")


# Heavily influenced by _wait_for_value function in epics_pvs.py, does block
def wait_for_value(signal: EpicsSignal, value, poll_time=0.01, timeout=10):
    expiration_time = ttime.time() + timeout
    current_value = signal.get()
    while current_value != value:
        ttime.sleep(poll_time)
        if ttime.time() > expiration_time:
            raise TimeoutError(
                "Timed out waiting for %r to take value %r after %r seconds"
                % (signal, value, timeout)
            )
        current_value = signal.get()


# Custom plan to move motor and then wait for laser pulse to take reading
def pulse_sync(detectors, motor, laser, start, stop, steps):
    step_size = (stop - start) / (steps - 1)

    for det in detectors:
        yield from bps.stage(det)

    yield from bps.open_run()
    for i in range(steps):
        yield from bps.checkpoint()  # allows pausing/rewinding
        yield from mv(motor, start + i * step_size)
        wait_for_value(
            laser.power, 0, poll_time=0.01, timeout=10
        )  # Want to be at 0 initially such that image taken on pulse
        wait_for_value(laser.power, 1, poll_time=0.001, timeout=10)
        yield from bps.trigger_and_read(list(detectors) + [motor] + [laser])
    yield from bps.close_run()

    for det in detectors:
        yield from bps.unstage(det)


prefix = "ADT:USER1:"
det = MyDetector(prefix, name="det")
det.hdf1.create_directory.put(-5)
det.hdf1.warmup()

det.cam.stage_sigs["image_mode"] = "Single"
det.cam.stage_sigs["acquire_time"] = 0.05

motor1 = EpicsMotor("motorS:axis1", name="motor1")

laser1 = MyLaser("laser:", name="laser1")
laser1.wait_for_connection()

RE = RunEngine()

bec = BestEffortCallback()
db = Broker.named("temp")  # This creates a temporary database

# Send all metadata/data captured to the BestEffortCallback.
RE.subscribe(bec)
# Insert all metadata/data captured into db.
RE.subscribe(db.insert)
