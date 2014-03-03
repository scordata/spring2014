"""
Adam Najman
HomeWork #2
closest_unsorted.py

This iterates through the list and checks the value
of temp for each element. Initially, temp is set to 
positive infinity. There's also a hash table to 
short circut the loop with (close to) constant lookups.

If the absolute value drops below the previous value,
and we havn't reached k numbers yet, we append the list
with a number beleived to be a target. At that point, we
raise the bar, to keep track of how many we've collected.

Runs in O(n + n) time: Iterates through n elements and does
n lookups.

"""


def find(arr, target, k):

  entered = {}
  retVal = []
  bar = 0
  temp = float('inf')
  for x in arr:
    foo = abs(target - x)
    if x in entered:
      retVal.append(x)
      bar+=1
      continue
    if foo <= temp:
      bar += 1
      temp = foo
      if bar <= k:
        entered[x] = True
        retVal.append(x)
      #print foo

  return retVal


print "first"
print find([4,1,3,2,7,4], 5.2, 2)
print "second"
print find([4,1,3,2,7,4], 6.5, 3)


