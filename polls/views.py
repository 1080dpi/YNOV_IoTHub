# -*- coding: utf-8 -*-
#!/usr/bin/python2.7
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .forms import NameForm

import httplib, urllib, base64, json, hmac, hashlib, time, requests, urllib2, json, hmac, ssl

connectionString = 'HostName=IoTpy.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=B29atBPWLBqQXKt0nAenWOvGpEbQVJNZpK6mnb878j4='
deviceId = 'PetitPython'

class D2CMsgSender():
    
    API_VERSION = '2016-02-03'
    TOKEN_VALID_SECS = 10
    TOKEN_FORMAT = 'SharedAccessSignature sig=%s&se=%s&skn=%s&sr=%s'
    
    def __init__(self, connectionString=None):
        if connectionString != None:
            iotHost, keyName, keyValue = [sub[sub.index('=') + 1:] for sub in connectionString.split(";")]
            self.iotHost = iotHost
            self.keyName = keyName
            self.keyValue = keyValue
            
    def _buildExpiryOn(self):
        return '%d' % (time.time() + self.TOKEN_VALID_SECS)
    
    def _buildIoTHubSasToken(self, deviceId):
        resourceUri = '%s/devices/%s' % (self.iotHost, deviceId)
        targetUri = resourceUri.lower()
        expiryTime = self._buildExpiryOn()
        toSign = '%s\n%s' % (targetUri, expiryTime)
        key = base64.b64decode(self.keyValue.encode('utf-8'))
        signature = urllib.quote(
            base64.b64encode(
                hmac.HMAC(key, toSign.encode('utf-8'), hashlib.sha256).digest()
            )
        ).replace('/', '%2F')
        return self.TOKEN_FORMAT % (signature, expiryTime, self.keyName, targetUri)
    
    def sendD2CMsg(self, deviceId, message):
        sasToken = self._buildIoTHubSasToken(deviceId)
        url = 'https://%s/devices/%s/messages/events?api-version=%s' % (self.iotHost, deviceId, self.API_VERSION)
        r = requests.post(url, headers={'Authorization': sasToken}, data=message)
        return r.text, r.status_code

def mapi(ville):
    baseurl = "https://query.yahooapis.com/v1/public/yql?"
    yql_query = "select item.condition from weather.forecast where woeid in (select woeid from geo.places(1) where text='%s')" % (ville)
    yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"
    result = urllib2.urlopen(yql_url).read()
    data_string = json.dumps(result, sort_keys=False, indent=6)
    data = json.loads(data_string)

    return data

def home(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            ville = form.cleaned_data['ville']

        current_ville = ville
        d2cMsgSender = D2CMsgSender(connectionString)
        message = mapi(ville)
        d2cMsgSender.sendD2CMsg(deviceId, message)
        
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'base.html', locals())
