#!/usr/bin/env python2
leases = '/var/lib/misc/dnsmasq.leases'
ip = None

while ( ip == None ):
	f = open(leases, 'r')

	for line in f:
       		if ( line.split(' ')[3] == 'raspberrypi' ):
               		ip = line.split(' ')[2]
			break
print ip
#print "192.168.0.102"
