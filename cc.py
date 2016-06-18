#!/usr/bin/python

import os, subprocess, time
from sys import platform as _platform

global total, toaddress, amount, cmd

total = 0

currency = str(sys.argv[1])
toaddress = str(sys.argv[2])
amount = str(sys.argv[3])

if _platform == "linux" or _platform == "linux2":
    # linux
    cmd = ('./' + currency + '-cli sendtoaddress ' + toaddress + ' ' + amount)
elif _platform == "darwin":
    # OS X
    cmd = ('./' + currency + '-cli sendtoaddress ' + toaddress + ' ' + amount) # guess same as linux?, needs testing
elif _platform == "win32":
    # Windows
    cmd = (currency + '-cli.exe sendtoaddress ' + toaddress + ' ' + amount) # needs testing

print 'running on: ' + _platform

def rpc():
    global total, toaddress, amount, cmd
    q = subprocess.check_output(cmd, shell=True)
    print q
    total = total + int(amount)
    print 'total sent: ' + str(total)
    time.sleep(6)
    rpc()

#shindig
rpc()



