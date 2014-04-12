"""
Google Code Jam
Problem d
Adam Najman
"""

from copy import deepcopy

i = open('input.txt', 'r')
o = open('output.txt', 'w')


tests = int(i.next())
print "test: ", tests

for line in xrange(tests):
  n = []
  k = []
  war_wins = 0
  dwar_wins = 0
  blocks = int(i.next())
  #print "blocks: ", blocks
  l = i.next().strip()
  n.append(map(float, l.split(' ')))
  h = i.next().strip()
  k.append(map(float, h.split(' ')))
  n[0].sort()
  k[0].sort()
  k2 = deepcopy(k)
  print n
  print k
  print k2

  for x in xrange(blocks):
    lie = True
    for y in xrange(len(k2[0])):
      if n[0][x] > k2[0][y]:
        lie = False
        break
    if lie:
      dwar_wins += 1
      del k2[0][-1]
        #break

  for x in xrange(blocks):
    n_chosen = n[0][x]
    #print "chosen: ", n_chosen
    for y in xrange(len(k[0])):
      #print "y", y
      if k[0][y] > n_chosen:
        #print "del!"
        del k[0][y]
        break

  war_wins = len(k[0])
  print "cheating she'll win, ", dwar_wins, " times"
  print "naomi could win ", war_wins , " times."

