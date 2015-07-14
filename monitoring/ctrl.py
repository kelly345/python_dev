#!/usr/bin/env Python
# __author__ = 'kelly'
# -*- coding: utf-8 -*-
import os, sys, time

while True:
    time.sleep(4)
    try:
        ret = os.popen('ps -C httpd -o pid,cmd').readlines()
        if len(ret) < 10:
            print "httpd process error,4 seconds restart!"
            time.sleep(3)
            os.system("service httpd restart")
    except:
        print "Error", sys.exc_info()[1]