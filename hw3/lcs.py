__author__ = "Adam Najman"
__filename__ = "lcs.py"
__homework_number__ = 3

from time import time
from collections import defaultdict

diagonal = -1
left = 0
up = 1


def topdown(s1, s2):
  return None

def bottomup(s1, s2):
  print "comparing " , s1 , " and " , s2
  for i in xrange(1, len(s1)):
    for j in xrange(1, len(s2)):
      if s1[i-1] == s2[j-1]:
        print "opt[",i,"][",j,"]= ", opt[i-1][j-1] + 1
        opt[i][j] = opt[i-1][j-1] + 1
        #print "back[",i,"][",j,"]= ", diagonal
        back[i][j] = diagonal
      elif opt[i-1][j] >= opt[i][j-1]:
        print "opt[",i,"][",j,"]= ", opt[i-1][j]
        opt[i][j] = opt[i-1][j]
        #print "back[",i,"][",j,"]= ", up
        back[i][j] = up
      else:
        print "opt[",i,"][",j,"]= ", opt[i][j-1]
        opt[i][j] = opt[i][j-1]
        #print "back[",i,"][",j,"]= ", left
        back[i][j] = left
      """
      if i == 0 or j == 0:
        opt[i][j] = 0
      if s1[i] == s2[i]:
        opt[i][j] = opt[i-1][j-1] + 1
      else:
        opt[i][j] = max( opt[i][j-1], opt[i-1][j] )
      """
  #print opt.values()
  print opt.keys()
  for foo in opt.keys():
    print foo, opt[foo]

  print back.keys()
  for bar in back.keys():
    print back[bar]
  print len(s1)
  print len(s2)


def backtrace(s, i, j):
  #print back
  print i, back[i], j
  print back[i][j]
  if i == 0 or j == 0:
    print "return"
    return
  if back[i][j] == diagonal:
    print "diagonal"
    backtrace(s, i-1, j-1)
    print s[i]
  elif back[i][j] == up:
    print "going up"
    backtrace(s, i-1, j)
  else:
    print "going left"
    backtrace(s, i, j-1)


f = open("lcsin.txt", 'r')
o = open("lcsout.txt", 'w')


def go(func, oper):
  for group in oper:
    opt = defaultdict(lambda: defaultdict(int))
    back = defaultdict(lambda: defaultdict(int))
    t = time()
    print func(group[0], group[1])
    if opt.keys() == []:
      print "NO LCS"
    print t - time()



lines = []

for line in f:
  lines.append(line.split())

#go(topdown, lines)
#go(bottomup, lines)

for group in lines:
  opt = defaultdict(lambda: defaultdict(int))
  back = defaultdict(lambda: defaultdict(int))
  t = time()
  print topdown(group[0], group[1])
  if opt.keys() == []:
    print "NO LCS"
  else:
    backtrace(group[0], len(group[0]), len(group[1]))
  print t - time()

for group in lines:
  opt = defaultdict(lambda: defaultdict(int))
  back = defaultdict(lambda: defaultdict(int))
  t = time()
  print opt, back
  print bottomup(group[0], group[1])
  if opt.keys() == []:
    print "NO LCS"
  else:
    print "backkeys is: ", back.keys(), len(back.keys())
    print "backvals is: ", back.values(), len(back.values())
    backtrace(group[0], len(back.keys()) - 1, \
              len(back.values()) - 2)
  print t - time()
