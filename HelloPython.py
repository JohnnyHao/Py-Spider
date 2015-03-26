__author__ = 'mll-001'

import  sys

import urllib2

from urllib2 import Request, urlopen, URLError, HTTPError


print "helle python"

print "hello tonny good study"

X = 'Span'
def func():
     X = 'NI!'
     print(X)

     def nested():
         print (X)
     nested()

func()
print(X)

print('######################################################################')
response = urllib2.urlopen('http://www.baidu.com/')
html = response.read()
print html

print('######################################################################')

req = urllib2.Request('http://www.baidu.com')
response = urllib2.urlopen(req)
the_page = response.read()
print the_page



old_url = 'http://www.baidu.com'
req = Request(old_url)
response = urlopen(req)
print 'Info():'
print response.info()

print('######################################################################')
print('######################################################################')


httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler, httpsHandler)
urllib2.install_opener(opener)
response = urllib2.urlopen('http://www.meilele.com')

import os.path
dir(os)