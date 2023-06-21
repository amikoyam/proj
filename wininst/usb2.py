#!/usr/bin/python3

import sys
from subprocess import PIPE, run

result = run('lsblk -do PATH,SUBSYSTEMS,SIZE', stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
print(result)

