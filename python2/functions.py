#!/usr/bin/python

def changeInt(a):
    a = 10

b = 2
changeInt(b)
print "value of int b is: " + str(b)

def changeMe( mylist ):
    # modify input list
    mylist.append([1, 2, 3, 4])
    print "Value in function: ", mylist
    return

mylist = [10, 20, 30]
changeMe( mylist )
print "Valud outside function: ", mylist
