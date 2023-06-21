#!/usr/bin/python3

import sys
import re
import subprocess

def usage(progname,exitvalue):
  print('Usage: ' + progname + ' boot-iso-image BMCNAME GFSPATH|HTTPURL [USBDRIVENAME]')
  print("GFSPATH - form of hostname:/path/to/folder/ISO_FILE.iso")
  print("HTTPURL - form of http://webpage.com/ISO_FILE.iso")
  print("          or https://webpage.com/ISO_FILE.iso")
  print("USBDRIVENAME - stripped form of device name such as sda, nvme0n1, etc. Not /dev/sda")
  exit(exitvalue)

def findusb():
  lsblk = subprocess.run(['lsblk', '-do', 'PATH,SUBSYSTEMS,SIZE'], check=True, capture_output=True)
  size = len(str(lsblk.stdout).split("\\n"))
  index=1
  usbln = ["" for x in range(size)]
  for line in str(lsblk.stdout).split("\\n"):
    if 'usb' in line:
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

  return device

def bootisoimage(bmcname, location, usbdrive):
  print('boot-iso-image')
  if re.match('http',location)
    print("web")
  else:
    print("FS")

# main

if len(sys.argv) < 2 or len(sys.argv) > 5:
  print('Syntax error!')
  usage(sys.argv[0],1)

if sys.argv[1] == '-h':
  usage(sys.argv[0],0)

if sys.argv[1] == 'boot-iso-image':
  if len(sys.argv) == 4:
    bootisoimage(sys.argv[2], sys.argv[3], findusb())
  if len(sys.argv) == 5:
    bootisoimage(sys.argv[2], sys.argv[3], sys.argv[4])


