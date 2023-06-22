import time as ttime
import argparse

import cothread
from softioc import builder, softioc

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--frequency", default=1, type=float)
parser.add_argument("-l", "--length", default=0.01, type=float, help="The pulse length")
parser.add_argument("--standalone", action="store_true", help="The pulse length")
# In standalone mode the power PV is set to 1 by an external signal generator pulse length remains set by this script

args = parser.parse_args()


# Tune properties of laser (not runtime configurable)
if not args.standalone:
    pulseLength = args.length
    frequency = args.frequency
    period = 1 / frequency
    assert period > pulseLength, "frequency is too high for pulse length"

else:
    frequency = -1
    pulseLength = args.length


# Device prefix
builder.SetDeviceName("laser")

# Create PV
laser = builder.boolOut("power", initial_value=0)
laser_freq = builder.aIn(
    "freq", initial_value=frequency
)  # This is simply for info, modifying the ai at runtime has no effect
pulse_id = builder.aIn("pulse_id", initial_value=0)
pulse_time = builder.aIn("pulse_time", initial_value=-1)

# Start IOC
builder.LoadDatabase()
softioc.iocInit()

if not args.standalone:

    def pulseLaser():
        while True:
            laser.set(0)
            cothread.Sleep(period - pulseLength)
            pulse_id.set(pulse_id.get() + 1)
            laser.set(1)
            pulse_time.set(ttime.time())
            cothread.Sleep(pulseLength)

else:
    poll_time = 0.001

    def pulseLaser():
        laser.set(0)
        while True:
            cothread.Sleep(poll_time)
            if laser.get() == 1:
                cothread.Sleep(pulseLength)
                laser.set(0)


cothread.Spawn(pulseLaser)

cothread.WaitForQuit()
