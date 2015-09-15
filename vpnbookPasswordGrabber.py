#!/usr/bin/python
from lxml import etree
import requests
from io import StringIO

def grabber():
	url = 'http://www.vpnbook.com/freevpn'
	load = requests.get( url )
	content = StringIO( u'' + load.content )
	parse = etree.parse( content, etree.HTMLParser() )
	parsed = parse.xpath( '//ul[@class="disc"]/li[text()="Password: "]/strong' )
	return 'No password found' if not len( parsed ) else parsed[ 0 ].text

print grabber()