```
four_nones = [None] \* 4
four_lists = [[] for \_\_ in range(4)]

letters = ['s', 'p', 'a', 'm']
word = ''.join(letters)

# Just check the value

if attr:
print 'attr is truthy!'

# or check for the opposite

if not attr:
print 'attr is falsey!'

# or, since None is considered false, explicitly check for it

if attr is None:
print 'attr is None!'

d = {'hello': 'world'}

print d.get('hello', 'default_value') # prints 'world'
print d.get('thingy', 'default_value') # prints 'default_value'

# Or:

if 'hello' in d:
print d['hello']

squares = [x**2 for x in range(10)]

from math import pi
[str(round(pi, i)) for i in range(1, 6)]

a = [3, 4, 5]
for i, item in enumerate(a):
print(i, item)

# prints

# 0 3

# 1 4

# 2 5

with open('file.txt') as f:
for line in f:
print line

name = input('What is your name?\n')
print('Hi, %s.' % name)

```
