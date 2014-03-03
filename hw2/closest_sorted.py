"""
Adam Najman
HomeWork#2
closest_sorted.py
"""

import bisect

def find(arr, target, k):

  temp = float('inf')
  retVal = []

  lo = 0
  hi = len(arr) 

  while k > 0 and lo <= hi:
    mid = (lo+hi)/2
    if temp > arr[mid]:
      foo = abs(target - arr[mid])
      k -= 1
      retVal.append(arr[mid])
    if arr[mid] > target:
      hi = mid-1
    elif arr[mid] < target:
      lo = mid+1
    else: 
      return mid
  return retVal



print "first"
print find([1,2,3,4,4,7], 5.2, 2)
print "second"
print find([1,2,3,4,4,7], 6.5, 3)
