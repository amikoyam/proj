#!/usr/bin/python3

import os
import re
import requests
import sys
import time

from urllib3.exceptions import InsecureRequestWarning
from requests.auth import HTTPBasicAuth

bmcip="10.45.145.201"
url = "https://" + bmcip + "/redfish/v1"
_auth = HTTPBasicAuth("debuguser", "0penBmc1")
# resp = requests.get('{}/Managers/bmc'.format(url), auth=_auth, verify=False)
print (requests.get('{}/Managers/bmc'.format(url), auth=_auth, verify=False))

