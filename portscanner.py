#!/bin/python3

import sys
import socket
from datetime import datetime

if len(sys.argv) > 4:
    if(sys.argv[3] == '-p'):
        if(len(sys.argv)> 5):
            p1 = int(sys.argv[4])
            p2 = int(sys.argv[5])+1

else:
    p1 = 1
    p2 = 65536

def helpfun():
    print("""
        Usage:
        ./portscanner.py [options] value [optional] value

        options: 
            -i      ip address
            -h      hostname
            -l      list of ip addresses or hostnames

        optional:
            -p      range of ports Ex: -p 80 8888 (default range 1 to 65535)
    """)
    sys.exit()

def elsefun():
    print('Invalid amount of arguments.')
    print('Use ./portscanner.py --help for more information')
    print('Exiting the program...')
    sys.exit()

def portscan(target):
    k = 1
    for port in range(p1,p2):
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
        print('Last Scanned port {}'.format(p2-1))
        print('No Ports open.\n\n')

def run(target):
    try:
        portscan(target)

    except KeyboardInterrupt:
        print('\n Exiting Program.')
        sys.exit()

    except socket.gaierror:
        print('Hostname could not be resolved.')
        sys.exit()

    except socket.error:
        print('Can not connect to server.')
        sys.exit()

if(len(sys.argv) == 1 ):
    helpfun()          

if len(sys.argv) >= 2:
    if(sys.argv[1] == '--help'):
        helpfun()  

    if(sys.argv[1] == '-i'):
        if(len(sys.argv) == 2):
            ip = input('Enter ip address: ')
            target = socket.gethostbyname(ip)
        else:
            target = socket.gethostbyname(sys.argv[2])
        print('-'*50)
        print('Scanning target '+target)
        print('Scan Started: '+str(datetime.now()))
        print('-'*50)
        run(target)

    if(sys.argv[1] == '-h'):
        if(len(sys.argv) == 2):
            host = input('Enter hostname: ')
            target = socket.gethostbyname(host)
        else:
            target = socket.gethostbyname(sys.argv[2])
        print('-'*50)
        print('Scanning target '+target)
        print('Scan Started: '+str(datetime.now()))
        print('-'*50)
        run(target)

    if(sys.argv[1] == '-l'):
        f = open( sys.argv[2], 'r' )
        iplists = f.read().split('\n')
        for target in iplists:
            print('-'*50)
            print('Scanning target '+target)
            print('Scan Started: '+str(datetime.now()))
            print('-'*50)
            run(target)
        
else:
    elsefun()

print('-'*50)
print('Scan Ended: '+str(datetime.now()))
print('-'*50)
sys.exit()