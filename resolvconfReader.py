#!/usr/bin/env python
def get_resolvers():
	resolvers = []
	try:
		with open( '/etc/resolv.conf', 'r' ) as resolvconf:
			for line in resolvconf.readlines():
				if 'nameserver' in line:
					resolvers.append( line.split( ' ' )[ 1 ].strip() )
		return resolvers
	except IOError as error:
		return error.strerror

<<<<<<< HEAD
print get_resolvers()
=======
print get_resolvers()
>>>>>>> f0b465f1fb37c2eb057577d0021d46c9e041f20f
