__author__ = "Adam Najman"
#__sources__ = "http://blog.codechef.com/2009/05/19/211/"

"""
Adam Najman
lcis.py

I orriginally used a n*m matrix, but realized
that the longest the sequence could be was n, 
where n = longest input string. This way, we
only need 2 lists: a current and a backtrack.

Any match is saved, and if theres a way to a
previous, smaller match, we update the backtrack
list. 

Printing is done by constructing a list of chars
corresponding to the backtrack list, and reverse
iterating through them.

"""

import sys


def lcis(words):
  a, b = words if len(words[0]) < len(words[1]) \
      else reversed(words)
  
  print " ", a, b

  bank = [0 for x in xrange(len(b))]
  prior = [0 for x in xrange(len(b))]

  for x in xrange(len(a)):
    current, last = 0, -1
    for y in xrange(len(b)):
      if a[x] == b[y] and current+1 > bank[y]:
        #print "match!", x, y
        prior[y] = last
        bank[y] = current+1
        #print "bank: ", bank
        #print "prior: ", prior
      if a[x] > b[y] and current < bank[y]:
        #print "greater than..."
        last = y
        current = bank[y]


  print "bank: ", bank
  print "prior: ", prior

  return bank, prior

def print_longest(bank, prior, word):
  lcis = []

  #x = len(word) - 1
  x = max(bank) - 1
  #if x == 0:
  #  x = -1
  print x
  while True:
    lcis.append(word[x])
    #a = raw_input()

    if x == -1: #or (x == 0 and (prior.index(x)==0)):
    #  lcis.append(word[prior.index(x)])
      break
    if x > -1:
      lcis.append(word[x])
    x = prior[x]
    print x
  #print "lcis", lcis
  for x in reversed(lcis): #faster than xrange
    #print x
    sys.stdout.write(str(x))
  print "\n"



f = sys.stdin#open('input.txt', 'r')
o = open('output.txt', 'w')


while True:
  foo = f.readline()
  if foo == '':
    break
  line = foo.split()
  print line
  bank, back =  lcis(line)
  word = line[0] if len(line[0]) >= len(line[1]) else line[1]
  print_longest(bank, back, word)
