# Lesson3
# Working with numbers and maths functions
from math import *
x = 5.7
y = 6.2
v =[x,y]
#% returns the whole number remainder
print(10%9)

# fmod() returns the real number down to decimal remainder 
# note:only works with floats
print(fmod(x,y))
#  this returns |x|

print(abs(x))

# this returns the lowest roundable value
print(floor(x))

# this returns largest roundable value
print(ceil(x))

# this rounds up the number to the specified index
print(round(x,0))

# this returns the rum of the iteratable list starting from the index specified
print(sum(v,0))

# this returns the maximum number from the list of numbers
print(max(v))
# returns the lowest number
print(min(v))

# combination mathematics
print(comb(5,3))
# this copies the sign of y and passes it on to x
print(copysign(x,-6))
# returns the redusal multiplication down to one,note:only accepts integers
print(factorial(5))
