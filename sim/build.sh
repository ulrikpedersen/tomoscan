#!/bin/bash

set -e

BUILD_DIRECTORIES="areaDetectorDock motorDock pmac pulsedLaser jupyter"

for DIR in $BUILD_DIRECTORIES; do
	echo "+--------------------------"
	echo "| Build $DIR"
	echo "+--------------------------"
	cd $DIR
	./build.sh
	cd ..
done
