#!/bin/bash
TOMOFILE=/home/bar/Projects/tomoscan

phoebus -resource "file:$TOMOFILE/display/overview.bob?P=ADT:USER1:&app=display_runtime"
