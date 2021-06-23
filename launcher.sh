#! /bin/sh
#launcher sh
cd /opt/gardenwatering/
sudo source env/bin/activate
sudo python3 GardenWatering.py 1> logs/gardenRun.txt &
sudo deactivate
cd /

