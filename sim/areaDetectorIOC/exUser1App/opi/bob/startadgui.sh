#!/bin/bash
AD=/home/bar/EPICS/support/areaDetector-master/ADCore/ADApp/op/bob/autoconvert/

phoebus -resource "file:$AD/ADBase.bob?P=ADT:USER1:&R=CAM:&app=display_runtime"
