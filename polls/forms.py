# -*- coding: utf-8 -*-
#!/usr/bin/python2.7
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
import base64, urllib2, json, hmac, hashlib, time, requests, urllib, ssl
from django import forms

class NameForm(forms.Form):
    ville = forms.CharField(label='Ville', max_length=100)
	
	# def send_data(self):
	# 	return self.ville