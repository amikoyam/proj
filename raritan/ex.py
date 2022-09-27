#!/usr/bin/python3
from raritan import rpc
from raritan.rpc import pdumodel
agent = rpc.Agent("https", "fl31ca105mp0301.deacluster.intel.com", "admin", 'R1C2021!')
pdu = pdumodel.Pdu("/model/pdu/0", agent)
outlets = pdu.getOutlets()
metadata = pdu.getMetaData()
print ("device information")
print (metadata)
print ("==================================================")
print ("outlet")
print (outlets[32].getSensors().current.getReading().value)


