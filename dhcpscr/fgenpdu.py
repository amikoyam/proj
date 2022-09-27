#!/usr/bin/python3
prefix = "10.45."
third = 252
nind = 240
offset = 30

for i in range(1,16):
    if nind > 255:
        third = third + 1
        nind = nind % 256
    print ("# RASP EMR Flexential 3 Floor 1 DataHall/Cage 1 Row 05 Aisle F Rack " + str(i) + " PDU")
    print ("# was RASP EMR Pod 1 Rack " + str(i+offset) + " PDU 4U CC")
    print ("subnet " + prefix + str(third) + "." + str(nind) + " netmask 255.255.255.248 {")
    print ("     option domain-name-servers 10.248.2.1, 10.22.224.204, 10.2.71.13;")
    print ('     option domain-name          "deacluster.intel.com";')
    print ('     option domain-search        "deacluster.intel.com intel.com";')
    print ("     option routers " + prefix + str(third) + "." + str(nind+1) + ";")
    print ("     option ntp-servers corp.intel.com;")
    print ('     include "/etc/dhcp/reservations/pod1-fl31ca105fr' + str(i).zfill(2) + '-pdu.conf";\n')
    print ("     next-server 10.45.128.101;")
    print ('     if exists user-class and option user-class = "iPXE" {')
    print ('         filename "http://10.45.128.101:8080/boot.ipxe";')
    print ("     } else {")
    print ('         filename "ipxe.efi";')
    print ("     }")
    print ("}\n")
    nind = nind + 8
