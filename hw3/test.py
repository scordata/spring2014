
bar = []
f = open("input.txt", 'r')

for line in f:
  print line
  l = line.strip()
  bar.append( map(int, l.split(' ')) )

print '-------------'
print f
print  bar


n = bar[0][0]
W = bar[0][1]

print "n is %i" % n
print "W is %i" % W

opt = [[] for n in range(n)]
print opt
print '--------------'



for x in opt:
  print x

