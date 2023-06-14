
#Register all support components
dbLoadDatabase "dbd/ioc.dbd"
ioc_registerRecordDeviceDriver(pdbbase)

#pmacAsynIPConfigure("geo1", "localhost:1025")
pmacAsynIPConfigure("geo1", "0.0.0.0:1025")
pmacCreateController("motorS","geo1",0,8,50,500)
pmacCreateAxis("motorS", 1)
pmacCreateAxis("motorS", 2)
pmacCreateAxis("motorS", 3)
pmacCreateAxis("motorS", 4)
pmacCreateAxis("motorS", 5)
pmacCreateAxis("motorS", 6)
pmacCreateAxis("motorS", 7)
pmacCreateAxis("motorS", 8)

# Load record instances
dbLoadRecords("config/ioc.db","P=motorS,M=:axis1")

iocInit()
