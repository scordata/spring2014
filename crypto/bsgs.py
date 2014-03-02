"""
Adam Najman
Cryptography
Problem set 1
Question 4c

Solving:
2^x = 92327518017225 (mod 247457076132467)
Tried this by brute force, and I don't think
I'm going to live long enough to find the answer.

See below for Shank's baby-step giant-step
"""

from math import sqrt

b = 92327518017225
# b is our beta
n = 2474570776132467
# n is our modulus

m = int(sqrt(n))
# m is the floor of the square root
# of n. We only have to calculate that
# high

giant = []
baby = []
# baby and giant are the two containers
# we are going to use to store the values

for x in range(0,m):
    giant.append( b * ( 2 ^ x ) % n )
print "giant is done"
# this is calculating the (mod n) of:
# beta * ( 2 XOR x )
# where x is going from 0 to m-1
# XOR is much faster here, as we can
# cheat a bit by using a form of 
# fast exponentiation

for y in range(1, m+1):
    baby.append( 2 ^ ( y * m ) % n )
print "baby is done"
# here we are storing (mod n):
# 2 XOR ( y * m )
# where y is going from 1 to m+1
# Again, we can cut corners with 
# XOR. 

print "The maximum from the intersection is: ", 
foo = max(set(giant).intersection(baby))
print foo
# We are going to need to perform operations
# on from the maximum of the intersection
# of the baby set and the giant set.
# Thus, foo = that number.


first = giant.index(foo)
second =  baby.index(foo)
# Here, we find the indexes of foo from their
# respective lists.

print "first is %i" % first
print "second is %i" % second

# we know that:
# x = second * m + first
# thus:
print "x equals: ", ( ( second + 1 ) * m - first ) % n

"""
OUTPUT:
giant is done
baby is done
The maximum from the intersection is:  885298502597643
first is 48003120
second is 17796712
x equals 885298454594521
"""
