#!/bin/bash
ADIOC=/home/bar/Projects/tomoscan/sim/areaDetectorIOC

phoebus -resource "file:$ADIOC/exUser1App/opi/bob/display.bob?P=ADT:USER1:&app=display_runtime"
