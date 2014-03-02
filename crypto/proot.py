import sys
sys.setrecursionlimit(1000000)

mem = {}
mem[0] = 1

for i in range(1,65537):
  mem[i] = 5 * mem[i-1]
  if 21 == mem[i] % 65537:
    print "FOUND IT",
    print "x is %i" % i
  
print "len of mem is: ",
print len(mem)

for i in range(65537):
  if i not in mem:
    print i,
    print " not found!"

print "end"
