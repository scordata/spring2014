"""
Adam Najman
HomeWork# 2
kmergesort.py

This function takes as arguments a list,
and k, where k is the number of divisions you want.

Work is k divisions, and log k for maintenience on
list of size n.

O(n * log(k))

"""

import heapq 

def kmergesort(arr, k):

  #Split the array into k parts
  n = [arr[i:i + k] for i in range(0, len(arr), k)]

  #Heapify each sublist
  for i in range(len(n)):
    heapq.heapify(n[i])

  retVal = []
  foo = []

  #Make a container (priority queue) for the first element
  #in each sublist
  #Tuple used to indicate the list origin (value, sublist)
  for x in range(len(n)):
    heapq.heappush(foo, (n[x][0], x))

  #While our list isn't sorted...
  while(len(retVal) < len(arr)):
  
    #pop off smallest value
    temp = heapq.heappop(foo)

    #add it to our sorted container
    retVal.append(temp[0])

    #remove it from the origin list
    del n[temp[1]][0]

    #bounds check
    if n[temp[1]] != []:
      #push next val on heap
      heapq.heappush(foo, (n[temp[1]][0], temp[1]))

  return retVal

print kmergesort([4,1,5,2,6,3,7,0], 3)
