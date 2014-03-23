
items = []
f = open("input.txt", 'r')

for line in f:
  print line
  l = line.strip()
  items.append( map(int, l.split(' ')) )

print '-------------'
print f
print  items


n = items[0][0]
W = items[0][1]
items = items[1:]


print "n is %i" % n
print "W is %i" % W
print "items is: "
print items


opt = [[] for n in items]
print "opt is: ", opt

temp = []

for x in items:
  print "test"
  for y in range(x[2]):
    print y
     
