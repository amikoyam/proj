#!/usr/bin/python3
# before processin, make sure to remove unwanted rack lines

import re

# fi = open("dhcpd.conf.r05e", "r")
# ft = open("etmp", "w+")
# fo = open("dhcpd.conf.r05e.new", "w")
# cnt = 0
offset = 45

with open("dhcpd.conf.r05e", "r") as fi:
  line = fi.readline()
  while line:
    if line.find ("# RASP Pod 1 Rack ") != -1:
      nums = [int(s) for s in re.findall(r"\d+",line)]
#       print (nums)
      cnt = nums[1] - offset
      etmp1 = re.sub (r"# RASP Pod 1 Rack \d+","# RASP EMR Flexential 3 Floor 1 DataHall/Cage 1 Row 05 Aisle E Rack " + str(cnt),line)
      etmp2 = re.sub (r"# RASP Pod 1 Rack ","# was RASP EMR Flexential Pod 1 Rack ",line.strip('\n'))
      etmp = etmp1 + etmp2 + " 4U CC"
    elif line.find ("option domain-name ") != -1:
      etmp = re.sub (r"fl30lse001.","",line.strip('\n'))
    elif line.find ("option domain-search ") != -1:
      etmp = re.sub (r"fl30lse001.deacluster.intel.com ","",line.strip('\n'))
    elif line.find ("include ") != -1:
      etmp = re.sub (r"rack\d+","fl31ca105er" + str(cnt).zfill(2),line.strip('\n'))
    else:
      etmp = line.strip('\n')
    print (etmp)
    line = fi.readline()

