"""
Adam Najman
HomeWork#2
closest_sorted.py

Since the list provided is sorted, we get to cheat
by using binary search. Temp is again set to positive 
infinity, to ensure a match.

Our bounds the limits of the array and we count
down from k, so we have the right amount of matches.

Binary search runs in O(log n), but we can shave some
time off of that by counting down from k.

Check the value, bisect the array, and divide accordingly.
Append to the return value list.

"""


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
  return retVal



print "first"
print find([1,2,3,4,4,7], 5.2, 2)
print "second"
print find([1,2,3,4,4,7], 6.5, 3)
