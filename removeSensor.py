import sys
import docker
import os
import subprocess

#Check script must run as root
if os.geteuid() != 0:
    sys.exit("Please run as root")


#Get ID Container

#Remove Container
proc = subprocess.run(['docker', 'ps', '-aq'], check=True, stdout=subprocess.PIPE, encoding='ascii')
container_ids = proc.stdout.strip().split()
print(container_ids)
if container_ids:
    subprocess.run(['docker', 'stop'] + container_ids, check=True)
    subprocess.run(['docker', 'rm'] + container_ids, check=True)
