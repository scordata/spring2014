

def lcis(words):
  a, b = words
  
  bank = [0 for x in xrange(len(b))]
  prior = [0 for x in xrange(len(b))]

  for x in xrange(len(a)):
    current, last = 0, -1
    for y in xrange(len(b)):
      if a[x] == b[y] and current+1 > bank[y]:
        bank[y] = current+1
        prior[y] = last
      if b[y]<a[x] and current<bank[y]:
        current = bank[y]
        last = y


  print "bank: ", bank
  print "prior: ", prior

  matrix = [['0' for x in xrange(len(a) + 1)] \
            for y in xrange(len(b) + 1)]

  #bank = OrderedDict() 

  #for i in xrange(len(a)):
  #  matrix[0][i+1] = a[i]
  #for i in xrange(len(b)):
  #  matrix[i+1][0] = b[i]

  


  """
  ma = 1
  for x in xrange(1, len(matrix)):
    for y in xrange(1, len(matrix[0])):
      if matrix[x][0] == matrix[0][y]:
        print "match!", matrix[x][0]
        print "(x, y):", (x, y)
        bank[matrix[x][0]] = (x,y)
        matrix[x][y] = str(ma)
        if x > bank.values()[-1][0] and \
           y >= bank.values()[-1][1]:
        #if [(x, y)] > bank.values(): #and matrix[x][0] in bank.keys():
          print "---hit"
          print (x, y)
          print bank.values()
          print matrix[x][y]
          matrix[x][y] = str(int(\
              matrix[bank.values()[-1][0]][bank.values()[-1][1]]) + 1)
          print "---"
            
  for elem in matrix:
    print elem
  print bank
  #print "bv: ", bank.values()[-1]
  """

  return bank, prior

def print_longest(prior, word):
  lcis = []

  x = len(word) - 1
  while x > -1:
    if x > -1:
      lcis.append(word[x])
    x = prior[x]
  print "lcis", lcis
  for x in reversed(lcis):
    print x,



f = open('input.txt', 'r')
o = open('output.txt', 'w')


while True:
  foo = f.readline()
  if foo == '':
    break
  line = foo.split()
  print line
  bank, back =  lcis(line)
  word = line[0] if len(line[0]) > len(line[1]) else line[1]
  print_longest(back, word)
