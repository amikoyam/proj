#!/usr/bin/python3

import sys
import re
import subprocess

lsblk = subprocess.run(['lsblk', '-do', 'PATH,SUBSYSTEMS,SIZE'], check=True, capture_output=True)
size = len(str(lsblk.stdout).split("\\n"))
index=1
usbln = ["" for x in range(size)]
for line in str(lsblk.stdout).split("\\n"):
  if 'usb' in line:
#   if 'dev' in line:
    usbln[index]=line
    index = index + 1
    print(index)

out=re.split("\s+", usbln[1])
device=re.split("/",out[0])[2]

if index == 1:
  print ("there is no USB device detected on the OS")
  exit(1)

if index > 2:
  print ("there are more than 1 USB drives.")
  for count in range(1, index):
    print (str(count)+". "+usbln[count])
    count = count + 1
  resp = input ("Please, select one: ")
  out=re.split("\s+", usbln[int(resp)])
  device=re.split("/",out[0])[2]

print(device)

