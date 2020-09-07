#!/bin/python3

import sys
import socket
from time import sleep
from datetime import datetime

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])

else:
    print('Invalid amount of arguments.')
    print('Syntax: python3 portscanner.py <ip>')
    print('Exiting the program...')
    sys.exit()

def portscan():
    k = 1
    for port in range(1,65536):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            k = k + 1
            print('Port {} is open '.format(port))
        scanupdate = 'Scanning port {}'.format(port)
        print (scanupdate, end='\r')
        s.close()
    if k == 1:
        print('No Ports open.')

print('-'*50)
print('Scanning target '+target)
print('Scan Started: '+str(datetime.now()))
print('-'*50)

try:
    portscan()

except KeyboardInterrupt:
    print('\n Exiting Program.')

except socket.gaierror:
    print('Hostname could not be resolved.')
    sys.exit()

except socket.error:
    print('Can not connect to server.')
    sys.exit()

print('-'*50)
print('Scan Ended: '+str(datetime.now()))
print('-'*50)
sys.exit()