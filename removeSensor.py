import sys
import docker
import os
import subprocess

#Check script must run as root
if os.geteuid() != 0:
    sys.exit("Please run as root")


#Shutdown Mata Elang Service
os.system("systemctl stop mataelang-snort.service")
print("Mata Elang Service Stopped")

#Remove Container
os.system("/usr/bin/docker container rm mataelang-sensor")
print("Mata Elang Sensor Deleted")