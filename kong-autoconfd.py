#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 1 - search3.py

import  sys
import  os
import httplib
import  urllib
import urllib2
import re
import cookielib
import  poster
import  json
import kong
import kubernetes
try:
    import json
except ImportError:  # for Python 2.5
    import simplejson as json

path = ('/api/v1/services')
inner_domain = "cluster.local"
outer_domain = "http://app.k8s.local"
kong_api = "http://10.99.11.1:31000"


kong = kong.client("http://10.99.11.1:31000")

connection = httplib.HTTPConnection('10.99.10.1:8080')
connection.request('GET', path)
rawreply = connection.getresponse().read()
reply = json.loads(rawreply)
#print reply["items"][0]

for i, val in enumerate(reply["items"]):
    print "########################\n" + str(i)
#    print json.dumps(val[i], indent=2)
# service 
#    print json.dumps(val, indent=2)
    print val["metadata"]["name"]
    print val["metadata"]["namespace"]
    print val["spec"]["ports"][0]["port"]
    ns = val["metadata"]["name"]
    svc = val["metadata"]["namespace"]
    port = val["spec"]["ports"][0]["port"]
    #always assume http
    protocol = "http" 
    inner_fullname = []
    inner_fullname.append(protocol)
    inner_fullname.append("://")
    inner_fullname.append(svc)
    inner_fullname.append(ns)
    inner_fullname.append(inner_domain)

#    inner_upstream = protocol + "://" + svc + ns + "svc" + inner_domain +":" + str(port)
    outer_fullname =  outer_domain + "/" + ns + svc
    

#    print json.dumps(val["spec"]["ports"], indent=2)
#    print json.dumps(reply["items"][i]["spec"], indent=2)
    
pretty_reply=json.dumps(reply,indent=2)
#print(pretty_reply)
#print(pretty_reply)
