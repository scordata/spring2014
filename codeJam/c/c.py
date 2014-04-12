"""
Google Code Jam
Problem c
Adam Najman
"""

i = open('input.txt', 'r')
o = open('output.txt', 'w')

def compute(R, C, M, mines):
  init = (R * C) - M
  print "init: ", init

  if M == 0:
    return

  elif init == 1:
    for r in xrange(R):
      for c in xrange(C):
        mines[r][c] = True
    return

  if R == 1 and C == 1:
    impossible = True
    print "IMPOSSIBLE!"
    return

  if R == 1 or C == 1:
    if init >= 2:
      for r in xrange(R-1, 0, -1):
        for c in xrange(C-1, 0, -1):
          if r > 1 or c > 1:
            mines[r][c] = True
            M -= 1
            if M == 0:
              return

      return
    else:
      impossible = True
      return
  
  elif init >= 4:
    if C > R:
      if M != R - 1:
        for r in xrange(R-1, 0, -1):
          mines[r][C-1] = True
          M -= 1
          if M == 0:
            return
        compute(R, C - 1, M, mines)
      else:
        if M == 1:
          mines[R - 1][C - 1] = True
          return
        for r in xrange(R-1, 2, -1):
          mines[r][C-1] = True
          M -= 1
        mines[R - 1][C - 2] = True
        return
    else:
      if M != C - 1:
        for c in xrange(C-1, 0, -1):
          mines[R-1][c] = True
          M -= 1
          if M == 0:
            return
        compute(R-1, C, M, mines)
      else:
        if M == 1:
          mines[R-1][C-1] = True
          return
        for c in xrange(C-1, 2, -1):
          mines[R-1][c] == True
          M -= 1
        mines[R-2][C-1] = True
  else:
    impossible = True
    return

tests = int(i.next())


for x in xrange(tests):

  impossible = False

  l = i.next().split()
  print l
  R = int(l[0])
  C = int(l[1])
  M = int(l[2])
  
  board = [[False for a in xrange(R)] \
          for b in xrange(M)]
  #print board
  print "R, C, M", R, C, M

  compute(R, C, M, board)

  print "Case#%i:" % x
  if impossible:
    print "Impossible"
    continue

  for r in xrange(R):
    for c in xrange(C):
      if r==0 and c==0:
        print 'c'
      elif board[r][c]:
        print '*'
      else:
        print '.'
