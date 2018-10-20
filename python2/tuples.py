#!/usr/bin/python

tup = ('physics', 'chemistry', 1997, 2000)

print tup
del tup
print "After deleting tup: "

try:
    print tup
except Exception as e:
    print e
