import os
import sys
import subprocess
import docker
import shutil
from os.path import abspath, dirname

#Check script must run as root
if os.geteuid() != 0:
    sys.exit("Please run as root")

#Check docker service in host
docker_service = subprocess.Popen(["systemctl", "is-active",  "docker"], stdout=subprocess.PIPE)
(output, err) = docker_service.communicate()
output = output.decode("utf-8")
output = output[:-1]

if output == "active":
    print("Docker service installed on your computer")
else:
    sys.exit("This service requires Docker, but your computer doesn't have it. Install Docker then try again. Aborting.")

#Get Current Directory Path
#file_directory = dirname(abspath(__file__))
current_directory = os.getcwd()

#Shutdown Mata Elang Service
os.system("systemctl stop mataelang-snort.service")

#Choose Rule
print("What kind rules do you want to use?\n\t1. Community\n\t2. Registered (required oinkcode)\n")
RULE_CHOICE = input("Rule Choice : ")

#Add condition to check rule choice from user
if (RULE_CHOICE != "1" and RULE_CHOICE != "2"):
    sys.exit("Choose a valid choice")

#Removing old container and old image
os.system("/usr/bin/docker container rm mataelang-sensor")
os.system("/usr/bin/docker image rm mataelang-snort")


#Pull Mata Elang Sensor Latest Version
os.system("/usr/bin/docker pull mataelang/snorqttalpine-sensor:latest")

#Condition to user when use community or Registered
if RULE_CHOICE == "1":
    os.system('docker tag mataelang/snorqttalpine-sensor:latest mataelang-snort')

if RULE_CHOICE == "2":
    print("I choose rule 2")
    #Build image with oinkcode

#Recreate Mata Elang Sensor
os.system('/usr/bin/docker create --name mataelang-sensor --network host -v /etc/localtime:/etc/localtime -v /etc/timezone:/etc/timezone --env-file /etc/mataelang-sensor/sensor.env mataelang-snort')
os.system('systemctl start mataelang-snort.service')

print("Mata Elang Sensor Success Updated")