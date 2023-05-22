TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = exercise
# exercise.dbd will be created and installed
DBD += exercise.dbd

# exercise.dbd will be made up from these files:
exercise_DBD += base.dbd
exercise_DBD += motorSupport.dbd
exercise_DBD += devSoftMotor.dbd
exercise_DBD += asyn.dbd
exercise_DBD += calcSupport.dbd
exercise_DBD += stream.dbd
exercise_DBD += drvAsynIPPort.dbd
exercise_DBD += pmacAsynMotorPort.dbd
exercise_DBD += pmacAsynIPPort.dbd


# exercise_registerRecordDeviceDriver.cpp derives from exercise.dbd
exercise_SRCS += exercise_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
exercise_SRCS_DEFAULT += exerciseMain.cpp

# Finally link to the EPICS Base libraries
exercise_LIBS += motor
exercise_LIBS += softMotor
exercise_LIBS += asyn
exercise_LIBS += seq
exercise_LIBS += pv
exercise_LIBS += stream
exercise_LIBS += calc
exercise_LIBS += pmacAsynMotorPort
exercise_LIBS += pmacAsynIPPort
exercise_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

# Sequencer flags - re-entrancy
exercise_SNCFLAGS += +r

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

