__author__ = "Adam Najman"
"""
Adam Najman
lcs_w_subseq.py
Python implementation of bottom-up (iterative)
LCS WITH a subsequence
Sources: CLRS, Python Docs

"""


import sys
#from collections import defaultdict


diag = 0
left = 1
up = 2


def subseq(s):
  if s == "":
    yield 0
  for dist, c in enumerate(s):
    yield c, dist


def lcs(words):
  a, b, c = words
  print a, b, c
  s = subseq(c)
  
  matrix = [[0 for x in xrange(len(b)+1)] \
               for y in xrange(len(a)+1)]

  back = [[0 for x in xrange(len(b)+1)] \
             for y in xrange(len(a)+1)]

  for i in xrange(1, len(a)+1):
    for j in xrange(1,len(b)+1):
      if a[i-1] == b[j-1]:
        #print "match at: ", i, j, a[i-1]
        test = next(s)
        #print "test: ", test
        if test[1] == len(c) - 1:
          #print "hit Max"
          s = subseq(c)
          continue
        if a[i-1] != test[0]:
          s = subseq(c)
        matrix[i][j] = matrix[i-1][j-1] + 1
        back[i][j] = diag
      elif matrix[i-1][j] > matrix[i][j-1]:
        matrix[i][j] = matrix[i-1][j]
        back[i][j] = up
      else:
        matrix[i][j] = matrix[i][j-1]
        back[i][j] = left


  for elem in matrix:
    print elem
  print "___"
  for elem in back:
    print elem
  print "---"

  backtrace(len(a), len(b), back, a)
  print "\n"

def backtrace(i, j, back, st):
  if i == 0 or j == 0:
    print "NO LCS"
    return 
  if back[i][j] == diag:
    backtrace(i-1, j-1, back, st)
    sys.stdout.write(st[i-1])
  elif back[i][j] == up:
    backtrace(i-1, j, back, st)
  else:
    backtrace(i, j-1, back, st)


f = sys.stdin#open('input.txt', 'r')

foo = f.readline()

while foo != "":
  lcs(foo.split())
  foo = f.readline()





