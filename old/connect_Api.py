#!/usr/bin/python2.7
# -*-coding:Utf-8 -*

import httplib, urllib, base64


def script():
    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': '6ad4f5df6daf4072adee64c65cd205eb',
    }

    params = urllib.urlencode({
        # Request parameters
        'q': 'PRISM eSport',
        'count': '10',
        'offset': '0',
        'mkt': 'fr-fr',
        'safesearch': 'Moderate',
    })

    try:
        conn = httplib.HTTPSConnection('api.cognitive.microsoft.com')
        conn.request("GET", "/bing/v5.0/search?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        return data
        conn.close()
    except Exception as e:
        return "[Errno {0}] {1}".format(e.errno, e.strerror)

api_data = script()

print(api_data)