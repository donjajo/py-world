#!/usr/bin/env python
resolvers = []
with open( '/etc/resolv.conf', 'r' ) as resolvconf:
	for line in resolvconf.readlines():
		if 'nameserver' in line:
			resolvers.append( line.split( ' ' )[ 1 ].strip() )
print resolvers