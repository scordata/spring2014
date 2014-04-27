


f = open('input.txt', 'r')
o = open('output.txt', 'w')

times = int(f.readline())


for x in xrange(times):
  nodes = int(f.readline())
  print nodes
  for y in xrange(nodes-1):
    fr, to = f.readline().split()
    fr = int(fr)
    to = int(to)

    print fr, to
