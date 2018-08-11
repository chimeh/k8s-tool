#!/usr/bin/python
# -*- coding: UTF-8 -*-
import  sys
import  os
import  urllib
import urllib2
import re
import cookielib
import  json
 
'''
dic = {'a': 'aa', 'b': 'bb'}
urllib.urlencode(dic)　　// dictionary 转成 url 中的参数: a=aa&b=bb
json.dumps(dic)　　// dictionary 转成 json: {"a":"aa", "b":"bb"}
'''
def jsonPost(url):
    print url
    print headers
    req=urllib2.Request(url,j_data,headers)
    page=urllib2.urlopen(req)
    result=page.read();
    print result;
    page.close();
 
headers={}
headers['Content-Type'] = 'application/json; charset=utf-8'
 
 
values={}
values['uuid']='xxx';
values['uid']='1234'
route='login'
port=8888
post_data=urllib.urlencode(values)
j_data=json.dumps(values);
print j_data
 
#pip install poster
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
#application/x-www-form-urlencoded
def test001():
    url = "http://www.example.com"
    body_value = {"package": "com.tencent.lian","version_code": "66" }
    body_value  = urllib.urlencode(body_value)
    request = urllib2.Request(url, body_value)
    #request.add_header(keys, headers[keys])
    result = urllib2.urlopen(request ).read()
 
#multipart/form-data
def test002():
    url = "http://www.example.com"
    body_value = {"package": "com.tencent.lian","version_code": "66" }
    register_openers()
    datagen, re_headers = multipart_encode(body_value)
    request = urllib2.Request(url, datagen, re_headers)
    # 如果有请求头数据，则添加请求头
    #request.add_header(keys,headers[keys])
    result = urllib2.urlopen(request ).read()
 
#application/json
def test003():
    url = "http://www.example.com"
    body_value = {"package": "com.tencent.lian","version_code": "66" }
    register_openers()
    body_value  = json.JSONEncoder().encode(body_value)
    request = urllib2.Request(url, body_value)
    #request.add_header(keys, headers[keys])
    result= urllib2.urlopen(request ).read()
 
test001();
test002();
test003();
 
#python http post json
#python实现http post四种请求体application/x-www-form-urlencoded ,multipart/form-data ,application/json,text/xml
#http://www.cnblogs.com/111testing/p/6079565.html
#http://www.cnblogs.com/hangj/p/4720628.html
#res = jsonPost("http://127.0.0.1:%s/%s" % (port, route))
#print res
