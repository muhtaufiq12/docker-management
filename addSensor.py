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


#Input User
PROTECTED_SUBNET = input("Protected Subnet : ")
EXTERNAL_SUBNET = input("External Subnet [default is any] : ")
EXTERNAL_SUBNET = "any"
ALERT_MQTT_TOPIC = input("MQTT Topic [default is snoqttv5] : ")
ALERT_MQTT_TOPIC = "snoqttv5"
ALERT_MQTT_SERVER = input("Mosquitto (MQTT Broker) IP : ")
ALERT_MQTT_PORT = input("Mosquitto (MQTT Broker) Port [default is 1883] : ")
ALERT_MQTT_PORT = "1883"
DEVICE_ID = input("Device ID : ")
#Show Available Network Interface
network_available = subprocess.Popen(["ls", "-C", "/sys/class/net"], stdout=subprocess.PIPE)
(result, err) = network_available.communicate()
result = result.decode("utf-8")
print("Available Network Interface : "+result)

NETINT = input("Network Interface : ")
COMPANY = input("Company : ")
print("What kind rules do you want to use?\n\t1. Community\n\t2. Registered (required oinkcode)\n")
RULE_CHOICE = input("Rule Choice : ")

#Add condition to check rule choice from user
if (RULE_CHOICE != "1" and RULE_CHOICE != "2"):
    sys.exit("Choose a valid choice")

#Pull MataElang image
docker_api = docker.from_env()
docker_api.images.pull('mataelang/snorqttalpine-sensor:latest')

#Make directory in /etc
os.makedirs("/etc/mataelang-sensor")

#Add Sensor Environment to /etc/mata-elangsensor
env_sensor_file = open("/etc/mataelang-sensor/sensor.env","w+")
env_sensor_file.write(
    'PROTECTED_SUBNET={0}\nEXTERNAL_SUBNET={1}\nALERT_MQTT_TOPIC={2}\nALERT_MQTT_SERVER={3}\nALERT_MQTT_PORT={4}\nDEVICE_ID={5}\nNETINT={6}\nCOMPANY={7}\n'
    .format(PROTECTED_SUBNET, EXTERNAL_SUBNET, ALERT_MQTT_TOPIC, ALERT_MQTT_SERVER, ALERT_MQTT_PORT, DEVICE_ID, NETINT, COMPANY)
)

#Copy mataelang-snort.service
src = current_directory + "/service/mataelang-snort.service"
#dst = "/home/taufiq/COBA/"
dst = "/etc/systemd/system/"
shutil.copy(src, dst)

#Condition to user when use community or Registered
if RULE_CHOICE == "1":
    docker_api.images.get('mataelang/snorqttalpine-sensor:latest').tag('mataelang-snort')

if RULE_CHOICE == "2":
    print("I choose rule 2")
    #Build image with oinkcode


#Regitering mata elang sensor service
#===Reload Daemon===#
daemon-reload = subprocess.Popen(["systemctl", "daemon-reload"])
#===Registering Mata Elang Snort Service===#
register-service = subprocess.Popen(["systemctl", "enable", "mataelang-snort.service"])
#===Create Container===#

#===Start Sensor===#
start-sensor = subprocess.Popen(["systemctl", "start", "mataelang-snort.service"])