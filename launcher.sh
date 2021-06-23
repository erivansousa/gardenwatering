#! /bin/sh
#launcher sh
cd /home/pi/gardenWatering/
sudo /usr/bin/python3 GardenWatering.py 1> logs/gardenRun.txt &
cd /

