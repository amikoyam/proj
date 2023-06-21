#!/usr/bin/python3

import sys
import re
import subprocess
import os


location = 'http://gfs-ro-flx3.deacluster.intel.com/gfs/ISO/Fedora-Server-dvd-x86_64-30-1.2.iso'
# location = 10.45.128.33:/images/ISO/PXE/WINDOWS/22ww51-6_BHS_RASP_r1/22ww51-6_BHS_RASP_r1.iso

if re.match('http', location)
  print("web")
else:
  print("FS")

