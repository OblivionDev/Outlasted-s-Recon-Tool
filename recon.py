#!/usr/bin/env python
# -*- coding: latin-1 -*- # ###################################################
#                                                                             #
#       Recon.py | By Outlasted                                               # 
#                                                                             #                                                                                                                                                           # 
#                                                                             #                                                                              
#                                                                             # 
###############################################################################

import socket
import subprocess
import sys
import urllib2
from datetime import datetime

# Clear the screen
subprocess.call('clear', shell=True)


print "=========================================="
print "   Welcome to Outlasted's recon scanner   "
print "=========================================="
print "      Identify your targets fast          "
print "==========================================\n"

remoteServer    = raw_input("Enter IP: ")
url = raw_input("Enter Website:")
remoteServerIP  = socket.gethostbyname(remoteServer)


print "-" * 60
print "Please wait scanning: ", remoteServerIP
print "-" * 60

t1 = datetime.now()



try:
    for port in range(1,1025):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print "=========================================="
            print "      Capturing Open Ports                "
            print "=========================================="
            print "Port {}: \t Open".format(port)
        sock.close()

except KeyboardInterrupt:
    print "You pressed Ctrl+C"
    sys.exit()

except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

except socket.error:
    print "Couldn't connect to server"
    sys.exit()

url.rstrip()
header = urllib2.urlopen(url).info()
print "=========================================="
print "      Capturing Website Header            "
print "=========================================="
print(str(header))


t2 = datetime.now()

total =  t2 - t1


print 'Scanning Completed in: ', total
print "Thanks for using Outlasted's recon scanner :3"
