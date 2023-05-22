< envPaths

cd "$(TOP)"

epicsEnvSet "EPICS_TS_MIN_WEST", '0'


# Loading libraries
# -----------------

# Device initialisation
# ---------------------

#Currently not creating a separate database for the simdetetector version
dbLoadDatabase "dbd/exUser1.dbd"
exUser1_registerRecordDeviceDriver(pdbbase)

# simDetectorConfig(const char *portName, int maxSizeX, int maxSizeY, int dataType,
#                   int maxBuffers, int maxMemory, int priority, int stackSize)
simDetectorConfig("SIM.CAM", 1024, 1024, 1, 1000, 0)

# ADCore path for manual NDTimeSeries.template to find base plugin template
epicsEnvSet "EPICS_DB_INCLUDE_PATH", "$(ADCORE)/db"

# NDProcessConfigure(portName, queueSize, blockingCallbacks, NDArrayPort, NDArrayAddr)
NDProcessConfigure("SIM.proc", 16, 0, "SIM.CAM", 0)

# NDFileTIFFConfigure(portName, queueSize, blockingCallbacks, NDArrayPort, NDArrayAddr)
NDFileTIFFConfigure("SIM.tiff", 16, 0, "SIM.CAM", 0)

# NDFileHDF5Configure(portName, queueSize, blockingCallbacks, NDArrayPort, NDArrayAddr)
NDFileHDF5Configure("SIM.hdf", 16, 0, "SIM.CAM", 0)

# NDPvaConfigure(portName, queueSize, blockingCallbacks, NDArrayPort, NDArrayAddr, pvName, maxBuffers, maxMemory, priority, stackSize)
NDPvaConfigure("SIM.pva", 16, 0, "SIM.CAM", 0, ADT:USER1:Pva1:ARRAY, 0, 0, 0, 0)
startPVAServer

# Final ioc initialisation
# ------------------------
cd "$(TOP)"
dbLoadRecords 'db/exUser1_expanded.db'
dbLoadRecords 'db/exUser1.db'
iocInit

# Extra post-init IOC commands
dbpf "ADT:USER1:HDF1:FileTemplate", "%s/%s_%d.h5"

dbpf "ADT:USER1:CAM:AcquirePeriod", "0.2"


