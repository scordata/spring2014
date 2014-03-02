import sys
sys.setrecursionlimit(1000000)

"""
  Adam Najman
  Homework #1
  ackermann.py
  LAST EDIT: 2/4//14
"""

'''
One of the reasons that Ackermann is so much
harder to computer than the Fibonacci function
has to do with the recursion depth and the
function definition. While both ackermann and
fibonacci grows exponentially, we can memoize
previous values of the fibonacci sequence 
for later access. This is possible with the 
ackermann function, but due to the oscillation
of the ackermann function it is less helpful.
Fibonacci only requires us to check a previous
value to compute the next. The Ackermann function
may require us to jump though many hoops before
we can find a previously indexed value.
'''


"""
  Use a dictionary 
  as an underlying 
  data structure for
  memoization
"""
memo = {}

# Standard Ackermann func
def A(m, n):
  if m == 0:
    return n+1
  elif m > 0 and n == 0:
    return A(m-1, 1)
  elif m > 0 and n > 0:
    return A(m-1, A(m, n-1))
  # For negative integers, Alpha-chars, etc.
  else:
    print ("Bad input")

def A2(m, n):
  """
   Initially tried this with a matrix
   via numpy - I learned that dictionaries
   have VERY useful built in functions for this
   Thank you, python docs.
  """
  if not hasattr(A2, "recCount"):
    A2.recCount = 1
  callBack = "A2( %d,"
  trace = "A2( %d, %d"
 # print callBack % (m)
  if m in memo and n in memo[m]:
    #print ("WORKS")
    return memo[m][n]
  else:
    #print ("ELSE")
    if m == 0:
      #print " m equals 0"
      if n > 1:
        print (callBack % (m)) * A2.recCount,
        print trace % (m,n) + (")" * A2.recCount + ")")
      retVal = n + 1
      A2.recCount -= 1
    elif m > 0 and n == 0:
      #print "first elif"
      A2.recCount -= 1
      print callBack % (m-1) * m,
      print (callBack % (m-1) + trace % (m-1, n+1) ) * m,
      print  (")"*m) + (")"*A2.recCount)
      retVal = A2(m-1, 1)
    elif m > 0 and n > 0:
      #print "second elif"
      print (callBack % (m-1)) * (A2.recCount),
      print (trace % (m, n-1) ) * m,
      print (")"*m)  + (")"*A2.recCount)
      A2.recCount += 1
      retVal = A2(m-1, A2(m, n-1))
    else:
      print ("Bad input")
    if m not in memo:
      #print "not in memo"
      memo[m] = {}
      memo[m, n] = retVal
  return retVal
  

