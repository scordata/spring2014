__author__ = "Adam Najman"
__filename__ = "lcs.py"
__homework_number__ = 3


"""
Longest Common Sub-sequence, based on the following 
algorithm from CLRS:

  if i == 0 or j == 0:
    opt[i][j] = 0
  if s1[i] == s2[i]:
    opt[i][j] = opt[i-1][j-1] + 1
  else:
    opt[i][j] = max(opt[i][j-1], opt[i-1][j] )

1 ) One example where top down is much faster than
    bottom up is the case of no LCS, such as:
    zzz and x:
    bottom up took: -0.000111818313599
    and had 0 non-zero cells
    top down took: -5.19752502441e-05
    and had 0 non-zero cells

2) One example where bottom up is much faster than
    top down are the two words:
      hieroglyphology and michelangelo
      bottom up took: -0.000566959381104
      and had 163 non-zero cells.
      top down took: -7.89525294304
      and had 156 non-zero cells

"""





from time import time
from collections import defaultdict

diagonal = -1
left = 0
up = 1
match = False

def topdown(i, j, s1, s2):
  if i == len(s1) or j == len(s2):
    return 0
  
  #print i, j, s1[i], s2[j]
  if s1[i] == s2[j]:
    match = True
    opt[i][j] = topdown(i+1, j+1, s1, s2) + 1
    back[i][j] = diagonal
  else:
    opt[i][j] = max( topdown(i, j+1, s1, s2), \
                     topdown(i+1, j, s1, s2))

  return opt[i][j]


def bottomup(s1, s2):
  match = False
  print "comparing " , s1 , " and " , s2
  for i in xrange(0, len(s1)):
    for j in xrange(0, len(s2)):
      #print i, j, opt[i][j]
      #print s1[i], s2[j]
      if s1[i] == s2[j]:
        match = True
        #print "opt[",i,"][",j,"]= ", opt[i-1][j-1] + 1
        opt[i][j] = opt[i-1][j-1] + 1
        #print "back[",i,"][",j,"]= ", diagonal
        back[i][j] = diagonal
      elif opt[i-1][j] >= opt[i][j-1]:
        #print "opt[",i,"][",j,"]= ", opt[i-1][j]
        opt[i][j] = opt[i-1][j]
        #print "back[",i,"][",j,"]= ", up
        back[i][j] = up
      else:
        #print "opt[",i,"][",j,"]= ", opt[i][j-1]
        opt[i][j] = opt[i][j-1]
        #print "back[",i,"][",j,"]= ", left
        back[i][j] = left
  return match


def backtrace(s, i, j):
  if i == 0 or j == 0:
    #print "return"
    print s[i]
    o.write(s[i])
    return
  if back[i][j] == diagonal:
    #print "diagonal"
    #print s[i]
    backtrace(s, i-1, j-1)
    print s[i]
    o.write(s[i])
  elif back[i][j] == up:
    #print "going up"
    backtrace(s, i-1, j)
  else:
    #print "going left"
    backtrace(s, i, j-1)


f = open("lcsin.txt", 'r')
o = open("lcsout.txt", 'w')

lines = []

for line in f:
  lines.append(line.split())


for group in lines:
  match = False
  opt = [[0 for y in range(len(group[1]) + 1)] \
            for x in range(len(group[0]) + 1 )]
  back =  [[0 for y in range(len(group[1]) + 1 )] \
            for x in range(len(group[0]) + 1 )]
  t = time()
  match =  bottomup(group[0], group[1])
  o.write("\n")
  for elem in opt:
    print elem
  if not match:
    print "NO LCS"
    o.write("NO LCS")
  else:
    backtrace(group[0], len(back) -2, len(back[0]) -2)
  print t - time()
  non_zero = 0
  for x in opt:
    for y in x:
      if y != 0:
        non_zero += 1
  print "non-zero cells:", non_zero

for group in lines:
  match = False
  opt = [[0 for y in range(len(group[1]) + 1)] \
            for x in range(len(group[0]) + 1 )]
  back =  [[0 for y in range(len(group[1]) + 1 )] \
            for x in range(len(group[0]) + 1 )]
  t = time()
  match =  topdown(0, 0, group[0], group[1])
  o.write("\n")
  if not match:
    print "NO LCS"
    o.write("NO LCS")
  else:
    backtrace(group[0], len(back) -2, len(back[0]) -2)
  print t - time()
  non_zero = 0
  for x in opt:
    for y in x:
      if y != 0:
        non_zero += 1
  print "non-zero cells:", non_zero

o.write("\n")

