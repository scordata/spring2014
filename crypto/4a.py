"""
Adam Najman
Cryptography
Problem set 1
Question 4a

This program checks to see
if 5 is a primitive root
mod 65537
"""

# A flag variable to show
# if it a primitive root.
# We assume it is.
flag = True

# A dictionary to store values
# of 5^x mod 65537
cache = {}

# This for loop stores all
# the values of 
# 5^x mod 65537
for i in range(65537):
  cache[i] = pow(5,i,65537)
  # The pow() function takes a base
  # an exponent, and its modulus.
  # It returns the base to the 
  # power, reduced by the modulus

# Here we check that we have a permutation
# of phi(65537). We know that the answer is
# 65536, as 65537 is prime, and the answer 
# to phi(prime) is prime - 1
# If there is a number missing then the flag
# will be set to false. 
for i in range(65537):
  if i not in cache:
    flag = False
    print cache[i]

if flag:
  print "5 is a primitive root"
else:
  print "5 is NOT a primitive root."

"""
OUTPUT:
5 is a primitive root
"""
