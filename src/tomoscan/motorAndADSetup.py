import time as ttime

from ophyd import ADComponent
from ophyd import AreaDetector, SingleTrigger
from ophyd import EpicsMotor
from ophyd.signal import EpicsSignal
from ophyd.areadetector import cam
from ophyd.areadetector.filestore_mixins import FileStoreHDF5IterativeWrite
from ophyd.areadetector.filestore_mixins import FileStoreTIFFIterativeWrite
from ophyd.areadetector.plugins import HDF5Plugin_V34, TIFFPlugin_V34
from bluesky import RunEngine
from bluesky.plans import count, scan
from bluesky.plan_stubs import mv


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


# Heavily influenced by _wait_for_value function in epics_pvs.py, does block
def wait_for_value(signal: EpicsSignal, value, poll_time=0.01, timeout=10):
    expiration_time = ttime.time() + timeout
    current_value = signal.get()
    while current_value != value:
        ttime.sleep(poll_time)
        if ttime.time() > expiration_time:
            raise TimeoutError(
                "Timed out waiting for %r to take value %r after %r second"
                % (signal, value, timeout)
            )
        current_value = signal.get()


# Custom plan to move motor and then wait for laser pulse to take reading
def pulse_sync(detector, motor, laser, start, stop, steps):
    step_size = (stop - start) / (steps - 1)
    for i in range(steps):
        yield from mv(motor, start + i * step_size)
        wait_for_value(
            laser, 0, poll_time=0.01, timeout=10
        )  # Want to be at 0 initially such that image taken on pulse
        wait_for_value(laser, 1, poll_time=0.01, timeout=10)
        yield from count(detector)


prefix = "ADT:USER1:"
det = MyDetector(prefix, name="det")
det.hdf1.create_directory.put(-5)
det.hdf1.warmup()

det.cam.stage_sigs["image_mode"] = "Single"
det.cam.stage_sigs["acquire_time"] = 1

motor1 = EpicsMotor("motorS:axis1", name="motor1")

laserStatus = EpicsSignal("laser:bi_power", name="laserStatus")

RE = RunEngine()
