import sys
from time import time
from collections import defaultdict
from random import randint, random

n = 20
W = 5000
# ws = [0, 5, 2, 5, 8, 8]
# vs = [0, 2, 16, 10, 15, 15]

ws = [0] + [randint(500, 1000) for _ in range(n)] #[0, 2, 1, 3]
vs = [0] + [randint(1, 20) for _ in range(n)] #[0, 4, 0.5, 5]

print ws
print vs

opt = defaultdict(lambda : defaultdict(int))
back = defaultdict(lambda : defaultdict(bool))

memoize = True

def search(i, w):
    if memoize and w in opt[i]: # memoization
        return opt[i][w]
    if i == 0 or w == 0:
        opt[i][w] = 0
    else:
        t1 = search(i-1, w) # better do it explicitly
        t2 = search(i-1, w-ws[i]) + vs[i] if w >= ws[i] else -1000
        if t2 > t1:
            opt[i][w] = t2
            back[i][w] = True
        else:
            opt[i][w] = t1
            back[i][w] = False
    return opt[i][w]

def bottomup(n, W):    
    for w in range(1, W+1):
        for i in range(1, n+1):
            t1 = opt[i-1][w]
            t2 = opt[i-1][w-ws[i]] + vs[i] if w >= ws[i] else -1000
            if t2 > t1:
                opt[i][w] = t2
                back[i][w] = True
            else:
                opt[i][w] = t1
                back[i][w] = False
    return opt[n][W]

def backtrace(i, w):
    if i == 0:
        return []
    return backtrace(i-1, w-ws[i]) + [True] if back[i][w] else backtrace(i-1, w) + [False]
    
t = time()
print search(n, W)
print time() - t
print backtrace(n, W)
print "non-zero cells:", sum(len(d) for d in opt.values())

opt = defaultdict(lambda : defaultdict(int))
back = defaultdict(lambda : defaultdict(bool))
t = time()
print bottomup(n, W)
print time() - t
print backtrace(n, W)            
print "non-zero cells:", sum(len(d) for d in opt.values())
