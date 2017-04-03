#!/usr/bin/env python
def get_resolvers():
	resolvers = []
	try:
		with open( '/etc/resolv.conf', 'r' ) as resolvconf:
			for line in resolvconf.readlines():
				line = line.split( '#', 1 )[ 0 ];
				line = line.rstrip();
				if 'nameserver' in line:
					resolvers.append( line.split()[ 1 ] )
		return resolvers
	except IOError as error:
		return error.strerror

print get_resolvers()
