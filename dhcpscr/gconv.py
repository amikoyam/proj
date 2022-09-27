#!/usr/bin/python3
# before processin, make sure to remove unwanted rack lines

import re

# fi = open("dhcpd.conf.r05g", "r")
# ft = open("gtmp", "w+")
# fo = open("dhcpd.conf.r05g.new", "w")
# cnt = 0

with open("dhcpd.conf.r05g", "r") as fi:
  line = fi.readline()
  while line:
    if line.find ("# RASP Pod 1 Rack ") != -1:
      nums = [int(s) for s in re.findall(r"\d+",line)]
#       print (nums)
      cnt = nums[1] - 15
      gtmp1 = re.sub (r"# RASP Pod 1 Rack \d+","# RASP EMR Flexential 3 Floor 1 DataHall/Cage 1 Row 05 Aisle G Rack " + str(cnt),line)
      gtmp2 = re.sub (r"# RASP Pod 1 Rack ","# was RASP EMR Flexential Pod 1 Rack ",line.strip('\n'))
      gtmp = gtmp1 + gtmp2 + " 4U CC"
    elif line.find ("option domain-name ") != -1:
      gtmp = re.sub (r"fl30lse001.","",line.strip('\n'))
    elif line.find ("option domain-search ") != -1:
      gtmp = re.sub (r"fl30lse001.deacluster.intel.com ","",line.strip('\n'))
    elif line.find ("include ") != -1:
      gtmp = re.sub (r"rack\d+","fl31ca105gr" + str(cnt).zfill(2),line.strip('\n'))
    else:
      gtmp = line.strip('\n')
    print (gtmp)
    line = fi.readline()

