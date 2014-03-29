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


def lis(sequence):
  
  retVal = []
  for x in range(len(sequence)):
    print "examining: ", sequence[x]
    #the following list comprehension checks for the
    #maximum length of the current subsequence
    #against the previous one
    #it's sort of abusing the boolean or operator,
    #because in python or returns the first non-false
    #value it finds - ie X or Y returns X if X is true
    # and Y if X is false and Y is true.
    # we append the current sequence value afterwards
    # to build out the return value
    temp = max([retVal[y] for y in xrange(0,x) \
                if retVal[y][-1] < sequence[x]] or [[]],\
                key=len)  + [sequence[x]]
    """
    retVal.append([[]])
    for d in range(x):
      print "loop number: ", d
      bar = [sequence[x]]
      print "bar is: ", bar
      if retVal[d] < sequence[x] or [[]]:
        bar = max([retVal[d]], key=len) + [sequence[x]]
        print "*bar is: ", bar
        #retVal.append(bar)
      retVal.append(bar)
    """
    print "temp is: ", temp
    print "retVal is: ", retVal

    #append the current subsequence to the list
    retVal.append(temp)

  #grab the largest subsequence by length
  retVal = max(retVal, key=len)
  return retVal


f = open("lisin.txt",'r')
o = open("lisout.txt", 'w')

ops = []

for line in f:
  print line
  ops.append(line.split())

print "ops is:", ops

for elem in ops:
  print list(elem[0])
  LIS = lis(list(elem[0]))
  print "LIS is: ", LIS
  LIS = ''.join(LIS)
  o.write("%s\n" % LIS)

