import cothread
from softioc import builder, softioc

# Device prefix
builder.SetDeviceName("laser")

# Create PV
laser = builder.boolIn("bi_power", initial_value=0)

# Tune properties of laser (should likely be PVs if trying to setup properly)
pulseLength = 0.5
frequency = 0.1
period = 1 / frequency
assert period > pulseLength, "frequency is too high for pulse length"

# Start IOC
builder.LoadDatabase()
softioc.iocInit()


def pulseLaser():
    while True:
        laser.set(0)
        cothread.Sleep(period - pulseLength)
        laser.set(1)
        cothread.Sleep(pulseLength)


cothread.Spawn(pulseLaser)

cothread.WaitForQuit()
