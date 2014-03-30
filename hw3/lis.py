"""
Sources:
  https://www.youtube.com/watch?v=4fQJGoeW5VE
  http://docs.python.org/2.7/library/functions.html#max
  http://docs.python.org/2/reference/expressions.html#or
  http://stackoverflow.com/a/4406777
"""
__author__ = "Adam Najman"
__filename__ = "lis.py"
__homework_number__ = 3


def topdown(seq):
  print "seq is: ", seq
  if len(seq) <= 1:
    return seq

  mark = 0
  sub = topdown(seq[1:])
  print "sub is: ", sub
  if seq[0] < sub[0]:
    print "returning ", [seq[0]] + sub
    return [seq[0]] + sub
  for i in range (1, len(seq)):
    if seq[i] > seq[i-1]:
      mark = i
      print "mark is: " , mark
    else: 
      break  
  recon = seq[:(mark + 1)]
  if len(recon) >= len(sub):
    print "recon is: ", recon
    return recon
  print "returning sub: ", sub
  return sub

def bottomup(seq):
  retVal = []
  for i in range(0, len(seq)):
    for j in range(i, -1, -1):
      print seq[j]
     # if seq[j] > seq[i]:
     #   print seq[j], ">" , seq[i]
     #   retVal.append(seq[j])
  return retVal


f = open("lisin.txt",'r')
o = open("lisout.txt", 'w')

ops = []

for line in f:
  print line
  ops.append(line.split())

print "ops is:", ops

o.write("Top Down Solution: \n")
print "Top Down Solution"

for elem in ops:
  print list(elem[0])
  LIS = topdown(list(elem[0]))
  print "LIS is: ", LIS
  LIS = ''.join(LIS)
  o.write("%s\n" % LIS)

o.write("Bottom Up Solution: \n")
print "Bottom Up Solution"

for elem in ops:
  print list(elem[0])
  LIS = bottomup(list(elem[0]))
  print "LIS is: ", LIS
  LIS = ''.join(LIS)
  o.write("%s\n" % LIS)

