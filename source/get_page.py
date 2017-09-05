#! /usr/bin/env python
#coding=utf-8
import urllib
import urllib2

def get_page(url):
    if not url.startswith('http://'):
        print "url error"
    else:
        a=urllib2.urlopen(url)
        print a.read()


get_page('http://www.ca.com')
    