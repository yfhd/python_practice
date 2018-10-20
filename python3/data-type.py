#!/usr/bin/python3

counter = 100
miles = 1000.0
name = "runoob"

print(counter)
print(miles)
print(name)

class A:
    pass

class B(A):
    pass

print(isinstance(A(), A))
print(type(A()) == A)
print(isinstance(B(), A))
print(type(B()) == A)

str = 'Runoob'
print(str)
print(str[0:-1])
print(str[0])
print(str[2:5])
print(str[2:])
print(str * 2)
print(str + "TEST")

print('Ru\noob')
print(r'Ru\noob')

word = 'Pythonn'
print(word[0], word[5])
print(word[-1], word[-6])
