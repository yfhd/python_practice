#!/usr/bin/python

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

del dict['Name']
dict.clear()
del dict

try:
    print "dict['Age']: ", dict['Age']
    print "dict['School']: ", dict['School']
except Exception as e:
    print e
