"""
Count occurences of a char in a string
"""
from collections import Counter 
from operator import itemgetter

foo = 'sqmvwtezknehmqljusenscippgmblcumouforqswulzcrxxtzrxnboaeqxvyfhrpcldaimteqdhbuzrqmpie\
fgibpfxrsogpmqjdmlpuiatldhibipoztnsdzhqkmjumeubokrgqbxndvcpetdpjtnuumxvdbkijttzfsobwgs\
ikveusljulymsctsmoimgzdrtxseuuicstojwwpcyzhnuzonyaulzzqxszgrpxpvumkpmlermcilfzqavoqkc\
bulyoimbypvewuwauibnlvdwczearxavendjxspmvewuzzzqkmtzfrhnathxqbemlgdsemhpnezrslrtqm\
hvyszbnvcjzzblnbeqcsogpmsyafmkcmbtpyaprorzzxdsppdjxsxqcywgtzhwqfoedrccprnvnnjfhqnjyf\
nxqjdnqijusumkfpcxcwlbcodljmqyzhnvammhcilfrsubxqkcjoogmjjtsunrjcwqsljuoafwkbcwzxvfle\
hljmenxxqfxigcrjyfgmbxpmjtrqtzfxrnpaetnbnqgeefyaciujrtsxxqlerefbjfgicjxq'

def stat(foo):
  ca = Counter(foo)
  print ca
  avg = []
  for x in ca:
        avg.append([x, ca[x]/(len(foo)/100.0)])
  	#avg.append([x, ca[x]/5.77])
  print sorted(avg, key=itemgetter(1), reverse=True)

stat(foo)

k0 = foo[0:len(foo):7]
k1 = foo[1:len(foo):7]
k2 = foo[2:len(foo):7]
k3 = foo[3:len(foo):7]
k4 = foo[3:len(foo):7]
k5 = foo[3:len(foo):7]
k6 = foo[3:len(foo):7]

print k0
print len(k0)
print k1
print len(k1)
print k2
print len(k2)
print k3
print len(k3)
print k4
print len(k4)
print k5
print len(k5)
print k6
print len(k6)

x = len(k0) + len(k1) + len(k2) + len(k3) + len(k4) + len(k5) + len(k6)
print x

print "k0 analisys"
stat(k0)
print "k1 analisys "
stat(k1)
print "k2 analisys "
stat(k2)
print "k3 analisys "
stat(k3)
print "k4 analisys "
stat(k4)
print "k5 analisys "
stat(k5)
print "k6 analisys "
stat(k6)
