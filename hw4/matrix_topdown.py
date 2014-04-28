__author__ = "Adam Najman"
#__sources__ == "CLRS"

"""
Adam Najman
Python implementation of top-down (recursive)
Matrix-chain Multiplication
Adapted from CLRS

"""



import re
import sys

def print_best(s, i, j):
  if i == j:
    sys.stdout.write("A%i" % i)
  else:
    sys.stdout.write("(")
    print_best(s, i, s[i][j])
    print_best(s, s[i][j]+1, j)
    sys.stdout.write(")")


def rec_matrix_order(p):
  n = len(p) - 1
  m = [[float("inf") for y in xrange(n + 1)] \
                     for x in xrange(n + 1)]
  #print m
  return lookup(m, p, 1, n)

def lookup(m, p, i, j):
  if m[i][j] < float("inf"):
    return m[i][j]
  elif i == j:
    m[i][j] = 0
  else:
    for k in xrange(i, j):
      q = ( lookup(m, p, i, k) + \
            lookup(m, p, k + 1, j) + \
            ( p[i-1]*p[k]*p[j] ) )
      if q < m[i][j]:
        m[i][j] = q
  return m[i][j]


f = sys.stdin#open('input.txt', 'rb')
times = int(f.readline())

delim = " ", "x", "\n"
patern = '|'.join(map(re.escape, delim))
#print "patern is: ", patern


for x in f:
    foo = re.split(patern, x)
    foo = foo[:-1]
    #print foo
    matrix = []
    for y in xrange(len(foo)):
        if y % 2 == 0:
            bar = (int(foo[y]), int(foo[y+1]))
            matrix.append(bar)
    print "matrix is: "
    print matrix
    param = []
    for e in matrix:
      param.append(e[0])
      if e == matrix[-1]:
        param.append(e[1])
    
    print "\n"
    print "rec: "
    print rec_matrix_order(param)
