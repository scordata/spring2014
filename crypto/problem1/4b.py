"""
Adam Najman
Cryptography
Problem Set 1
Question 4b

A brute force check to determine
the solution to:
5^x = 21 (mod 65537)
"""


# A dictionary to linearize
# our calculations
mem = {}
mem[0] = 1

# The for loop iterates from
# 1 until 65536. If a match is
# found, it reports it

for i in range(1,65537):
  mem[i] = 5 * mem[i-1]
  if 21 == mem[i] % 65537:
    print "FOUND IT",
    print "x is %i" % i

# Print the length to prove
# we've iterated over all the 
# options
print "len of mem is: ",
print len(mem)

# This checks for errors in hash
# storage. Verifies our calculation
for i in range(65537):
  if i not in mem:
    print i,
    print " not found!"

print "end"

"""
OUTPUT:
FOUND IT x is 18000
len of mem is:  65537
end
"""
