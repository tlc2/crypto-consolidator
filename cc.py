#!/usr/bin/python

import os, sys, subprocess, time

global total, fromaccount, toaddress, amount, cmd

total = 0

currency = str(sys.argv[1])
fromaccount = str(sys.argv[2])
toaddress = str(sys.argv[3])
amount = str(sys.argv[4])

cmd = ('./' + currency + '-cli sendfrom ' + fromaccount + ' ' + toaddress + ' ' + amount)

def rpc():
    global total, fromaccount, toaddress, amount, cmd
    q = subprocess.check_output(cmd, shell=True)
    print q
    total = total + int(amount)
    print 'total : ' + str(total)
    time.sleep(6)
    rpc()

rpc()




