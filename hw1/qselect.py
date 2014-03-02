"""
Adam Najman
HW#1
qselect.txt
LAST EDIT: 2/4/14
"""

from random import choice

"""
I'm getting weird off-by-one errors with this
configuration. I'm running out of time to find
the bug. If running optimally, CLRS claims
that a quick select algorithm maintains
a Theta(n) run-time.

This uses a counter to measure how often
we encounter the pivot at each recursion 
level. This along with the length of 
a list, can be used to measure the
distance left to go.

CLRS moved the partitioning outside
of the main function - I tried to include it.
Perhaps that's where my error lies.
"""
# With help from CLRS
def qselect(val, ops):
 
  print "val is %i" % val

 # if not hasattr(qselect, "counter"):
 #   qselect.counter = 0

  #if empty list, you've
  #found you're nth smallest element
  if len(ops) == 1:
    return ops[0]

  if ops != []:
    #as long as list isn't empty...
    
    #to measure the nth smallest element
    counter = 0

    piv = choice(ops)
    #randomly select a pivot

    #array partitions
    lThan = [] #the Less than array'
    gThan = [] #the Greater than array'

    print "piv is: %i" % piv
    print "counter is: %i" % counter

    print "lThan is: "
    print lThan
    print "gThan is: "
    print gThan

    print "ops is: "
    print ops


    #Start partitioning
    for element in ops:
      if element == piv:
        counter += 1
        print "counter incremented! %i" % counter
      elif element > piv:
        gThan.append(element)
        print "%i is > than %i" % (element, piv)
      else:
        lThan.append(element)
        print "%i is < %i" % (element, piv)
    
    #CLRS says you can use the array sizes to
    #figure out the element you're looking for
    print "lThan has size: %i" % len(lThan)
    print "and contains: "
    print lThan

    print "gThan has size: %i" % len(gThan)
    print " and contains: "
    print gThan

    if val < len(lThan):
      print "val is < lThan"
      return qselect(val, lThan)
    elif val <= len(lThan) + counter:
        print "val < len(lThan) + counter"
        return piv
    elif val > len(lThan) + counter:
      print "going with gThan"
      val = val - len(lThan) + counter
      return qselect(val, gThan)



if __name__ == "__main__":
  print "qselect(2, [3,10,4,7,19])"
  print qselect(2, [3,10,4,7,19])
  print "-----------------------"
  print "qselect(4, [11,2,8,3])"
  print qselect(4, [11,2,8,3])


