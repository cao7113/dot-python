#!/usr/bin/env python

# single line comment
print("Hello, World!")

def my_function():
  print("Hello from a function")

my_function()

print __name__ # __main__

def fun1():
    print 'fun1'

def fun2():
    print 'fun2'
    fun1()

fun2()
