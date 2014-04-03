import sys
from time import time
from collections import defaultdict
from random import randint

n = 5
W = 20
ws = [0,5,2,5,8,8]#[0] + [randint(1, 10) for _ in range(n)]#[0,2,3]
vs = [0,2,16,10,15,15]#[0] + [randint(1, 20) for _ in range(n)]  # [0,4,5]

print ws
print vs

opt = defaultdict(lambda : defaultdict(int))
#back pointers
back =  defaultdict(lambda : defaultdict(bool))
#top down
def search(i,w):
  if (i, w) in opt:
    return opt[i][w]
  if i == 0 or w == 0:
    opt[i][w] = 0
  else:
    search(i-1, w)
    if w >= ws[i] and search(i-1, w-ws[i]) + vs[i] >\
                     opt[i-1][w]:
      opt[i][w] = opt[i-1][w-ws[i]] + vs[i]
      back[i][w] = True
    else:
       opt[i][w] = opt[i-1][w]
       back[i][w] = False
  return opt[i][w]

#bottomup
def bottomup(n, W):
  for w in range(1, W+1):
    for i in range(1, n+1):
      if w >= ws[i] and opt[i-1][w-ws[i]] + vs[i] >\
          opt[i-1][w]:
        opt[i][w] = opt[i-1][w-ws[i]] + vs[i]
        back[i][w] = True
      else:
        opt[i][w] = opt[i-1][w]
        back[i][w] = False
  return opt[n][W]

def backtrace(i, w):
  if i == 0:
      return []
  if back[i][w]:
    return backtrace(i-1, w-ws[i]) + [True]
  return backtrace(i-1, w) + [False]


t = time()
print search(n, W)
print time() - t
print backtrace(n, W)
for i in range(1, n+1):
  print i,  opt[i]

opt = defaultdict(lambda : defaultdict(int))
#back pointers
back =  defaultdict(lambda : defaultdict(bool))
t = time()
print bottomup(n, W)
print time() - t
print backtrace(n, W)
for i in range(1, n+1):
  print i,  opt[i]
