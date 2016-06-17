#!/usr/bin/python

import os, sys, subprocess, time

global total, toaddress, amount, cmd

total = 0

currency = str(sys.argv[1])
toaddress = str(sys.argv[2])
amount = str(sys.argv[3])

cmd = ('./' + currency + '-cli sendtoaddress ' + toaddress + ' ' + amount)

def rpc():
    global total, toaddress, amount, cmd
    q = subprocess.check_output(cmd, shell=True)
    print q
    total = total + int(amount)
    print 'total sent: ' + str(total)
    time.sleep(6)
    rpc()

rpc()



