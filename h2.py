n = 500
import random

x = [random.randint(0,100) for _ in xrange(n)]

y = [random.randint(0,100) for _ in xrange(n)]


z = [a+b for a in x for b in y]


z.sort()

# import heapq for this
#a = O(n^2logn@) = O(n^2logn)
#b = O(n^2)
#c = O(nlogn)
# for c sort a sort b, then build priority queue for a+b
# build a frtontier algorithm
#PQ rests on a binary heap
#pull [0] and replace with [-1]
#check (and swap) [i+1] and [i+2] recursivly until
# match found
# for insert check floor(i/2) (bubble up)
# for delete bubble down

sum = i,j, heapq.pop(pq)
heapq.push(blah)
heapq.push(bleah)
restult.append(blah)

#xrange (num) is the lazy version of range(num)
#push sum, y val, i, j

#DATA STREAMS:
#find k smallest numbers in a data stream (can't store)
# of length n. with only O(K) space.
