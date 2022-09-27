#!/usr/bin/python3
# before processin, make sure to remove unwanted rack lines

import re

# fi = open("dhcpd.conf.r05h", "r")
# ft = open("htmp", "w+")
# fo = open("dhcpd.conf.r05h.new", "w")

with open("dhcpd.conf.r05h", "r") as fi:
  line = fi.readline()
  while line:
    if line.find ("# RASP Pod 1 Rack ") != -1:
      htmp1 = re.sub (r"# RASP Pod 1 Rack ","# RASP EMR Flexential 3 Floor 1 DataHall/Cage 1 Row 05 Aisle H Rack ",line)
      htmp2 = re.sub (r"# RASP Pod 1 Rack ","# was RASP EMR Flexential Pod 1 Rack ",line.strip('\n'))
      htmp = htmp1 + htmp2 + " 4U CC"
    elif line.find ("option domain-name ") != -1:
      htmp = re.sub (r"fl30lse001.","",line.strip('\n'))
    elif line.find ("option domain-search ") != -1:
      htmp = re.sub (r"fl30lse001.deacluster.intel.com ","",line.strip('\n'))
    elif line.find ("include ") != -1:
      nums = [int(s) for s in re.findall(r"\d+",line)]
#       print (nums[1])
      if nums[1] > 9:
        htmp = re.sub (r"rack","fl31ca105hr",line.strip('\n'))
      else:
        htmp = re.sub (r"rack","fl31ca105hr0",line.strip('\n'))
    else:
      htmp = line.strip('\n')
    print (htmp)
    line = fi.readline()



