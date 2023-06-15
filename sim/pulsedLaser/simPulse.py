import time as ttime

import cothread
from softioc import builder, softioc

# Device prefix
builder.SetDeviceName("laser")

# Tune properties of laser (not runtime configurable)
pulseLength = 0.01
frequency = 1
period = 1 / frequency
assert period > pulseLength, "frequency is too high for pulse length"

# Create PV
laser = builder.boolIn("power", initial_value=0)
laser_freq = builder.aIn(
    "freq", initial_value=frequency
)  # This is simply for info, modifying the ai at runtime has no effect
pulse_id = builder.aIn("pulse_id", initial_value=0)
pulse_time = builder.aIn("pulse_time", initial_value=-1)

# Start IOC
builder.LoadDatabase()
softioc.iocInit()


def pulseLaser():
    while True:
        laser.set(0)
        cothread.Sleep(period - pulseLength)
        pulse_id.set(pulse_id.get() + 1)
        laser.set(1)
        pulse_time.set(ttime.time())
        cothread.Sleep(pulseLength)


cothread.Spawn(pulseLaser)

cothread.WaitForQuit()
