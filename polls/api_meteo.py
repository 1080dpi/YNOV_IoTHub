# -*- coding: utf-8 -*-
#!/usr/bin/python2.7
from __future__ import unicode_literals
import urllib2, urllib, json

def mapi(ville):
	baseurl = "https://query.yahooapis.com/v1/public/yql?"
	yql_query = "select item.condition from weather.forecast where woeid in (select woeid from geo.places(1) where text='%s')" % (ville)
	yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"
	result = urllib2.urlopen(yql_url).read()
	data_string = json.dumps(result, sort_keys=False, indent=6)
	data = json.loads(data_string)

	return data

print mapi('Lyon')