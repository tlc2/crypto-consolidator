#!/usr/bin/python

import os, subprocess, time
from sys import platform as _platform

global total, toaddress, amount, cmd

total = 0

currency = str(sys.argv[1])
toaddress = str(sys.argv[2])
amount = str(sys.argv[3])

# determine platform
if _platform == "linux" or _platform == "linux2":
    # linux
    cmd = ('./' + currency + '-cli sendtoaddress ' + toaddress + ' ' + amount)
elif _platform == "darwin":
    # OS X
    cmd = ('./' + currency + '-cli sendtoaddress ' + toaddress + ' ' + amount) # posix so guess same as linux?, needs testing
elif _platform == "win32":
    # Windows
    cmd = (currency + '-cli.exe sendtoaddress ' + toaddress + ' ' + amount) # needs testing

#print 'running on: ' + _platform

def rpc():
    global total, toaddress, amount, cmd
    q = subprocess.check_output(cmd, shell=True)
    print q # txid of transaction
    total = total + int(amount)
    print 'total sent: ' + str(total)
    time.sleep(6) # box tested on took about 4-5 secs to build and broadcast a complex tx and be ready for more input
    rpc()

#shindig
rpc()



