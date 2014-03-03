"""
Adam Najman
HomeWork#2
datastream.py

For this problem, we can just simulate a hardware cache.
After defining the cache size (num) we blindly accept
the first k elements.

From then on, we compare the value of the new k to
the value at store[k%num]. This is a constant time
comparison. Depending on the value, we overwrite.

Since we need the final output sorted, but
are limited to O(k) space, we should use insertion sort.
Insertion sort yields time complextity of O(n^2) and
space complexity of O(1).

Thus, this algorithim keeps track of the smallest
values while they are fed in. This runs in O(n + k^2),
where, n is the size of the datastream and k is our saved
values. Excluding the datastream buffer, we only need 
O(k) space. It's too bad that the final output needs to 
be sorted, otherwise we could run in O(n).
(Try printing store without sorting it to see what I mean)

"""

import heapq

def ds():
  print "enter max size:"
  num = input()
  store = []
  count = 0
  print "max size is: %i" % num
  
  print "enter items one at a time (-1 to exit):"
  foo = input()
  while (True):
    
    foo = input()
    if foo == -1:
      break;

    if count < num:
      store.append(foo)
      count += 1

    else:
      if (foo < store[foo%num]):
        store[foo%num] = foo
    
  store = insert_sort(store)

  print store

#From CLRS / csci 111
#Takes n^2 time but is O(1) 
#on space, and that's a hard constraint
def insert_sort(a):
  for i in range(len(a)):
    j = i-1
    val = a[i]
    while(a[j] > val) and (j >= 0):
      a[j+1] = a[j]
      j -= 1
    a[j+1] = val

  return a

ds()
