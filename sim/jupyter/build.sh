#!/bin/bash
DIR=$(pwd)
cd ../..
docker build -t tomoscan_jupyter -f sim/jupyter/Dockerfile .
cd $DIR