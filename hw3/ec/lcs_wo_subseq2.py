import sys
sys.setrecursionlimit(1000000000)

diagonal = -1
left = 0
up = 1

def virus(v):
  #print "input was ", v
  if v == "":
    #print "empty virus"
    yield 0
  for dist, elem in enumerate(v):
    #print "dist, elem: ", dist, elem
    yield elem, dist


def backtrace(s, i, j):
  #print "i, j, s[i]: ", i, j, s[i]
  if i == 0 or j == 0:
    #print i, j, s[i]
    print "NO LCS"
    return
  if back[i][j] == diagonal:
    #print s[i]
    backtrace(s, i-1, j-1)
    print s[i]
  elif back[i][j] == up:
    backtrace(s, i-1, j)
  else:
    backtrace(s, i, j-1)


def lcs(seq):
  x, y, z = seq
  print x, y, z
  v = virus(z)
  #print next(v)
  string_set = [[0 for h in xrange(len(y) + 1)] \
                   for i in xrange(len(x) + 1)]
  for i in xrange(0, len(x)):
    for j in xrange(0, len(y)):
      if x[i] == y[j]:
        check = next(v)
        #print "check: ", x[i], check[0]
        if check[1] == len(z) - 1:
          v = virus(z)
          continue
        if x[i] != check[0]:
          v = virus(z)
        string_set[i+1][j+1] = string_set[i][j] + 1
        back[i+1][j+1] = diagonal
      elif string_set[i][j+1] >= string_set[i+1][j]:
          string_set[i+1][j+1] = string_set[i][j+1]
          back[i+1][j+1] = up
      else:
        string_set[i+1][j+1] = string_set[i+1][j]
        back[i+1][j+1] = left
        #string_set[i+1][j+1] = max( string_set[i+1][j],\
        #                        string_set[i][j+1] )

  return string_set




test_seq = [["XMJYAUZ","MZJAWXU","JA"],
            ["abcbdab", "bdcaba", "bca"], 
            ["zzz", "zz", "z"]]

print "BOTTOM UP SOLUTIONS:"
for x, case in enumerate(test_seq):
  back = [[0 for i in xrange(len(test_seq[x][1]) + 1)] \
            for j in xrange(len(test_seq[x][0]) + 1)]
  #print x, case
  foo = lcs(case)
  top = "   #  "
  bot = "#"
  for qux in case[1]:
    top += qux + "  "
  print top
  for letter in case[0]:
      bot += letter
  #print "bot is: ", bot
  for elem, bar in enumerate(foo):
    #print case, x, elem, bar
    #print case[x][elem], bar
    print bot[elem], bar
  for elem in back:
    print elem
  print "LCS IS: "
  backtrace(test_seq[x][0], len(back)-2, len(back[0])-1)
print "\n-----------------------\n"

