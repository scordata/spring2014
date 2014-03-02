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
ca = Counter(foo)
print ca
avg = []
for x in ca:
	avg.append([x, ca[x]/5.77])
print sorted(avg, key=itemgetter(1), reverse=True)

print "bigram analysis"
bg = []
for i in range(len(foo) - 1):
	tmp = foo[i] + foo[i+1]
	for j in range(len(foo)-1):
		bar = foo[j] + foo[j+1]
		if tmp == bar and j - i < 13 and j - i > 2:
			print "match!",
			print tmp,
			print i,
			print bar,
			print j,
			print "possible key size: %i" % (j-i)
			bg.append([tmp, j-i])

print "trigram analisys"
tg = []
for i in range(len(foo) - 2):
	tmp = foo[i] + foo[i+1] + foo[i+2]
	for j in range(len(foo)-2):
		bar = foo[j] + foo[j+1] + foo[j+2]
		if tmp == bar and j - i > 0: #and j - i > 2:
			print "match!",
			print tmp,
			print i,
			print bar,
			print j,
			print "possible key size: %i" % (j-i)
			tg.append([tmp, j-i])

print "quadgram anaylisys"
qg = []
for i in range(len(foo) - 3):
	tmp = foo[i] + foo[i+1] + foo[i+2] + foo[i+3]
	for j in range(len(foo)-3):
		bar = foo[j] + foo[j+1] + foo[j+2] + foo[j+3]
		if tmp == bar and j - i > 0: #and j - i > 2:
			print "match!",
			print tmp,
			print i,
			print bar,
			print j,
			print "possible key size: %i" % (j-i)
			qg.append([tmp, j-i])

print "lists:"
print "bg: "
print bg
print "tg: "
print tg
print "qg: "
print qg

for x in bg:
	for y in tg:
		for z in qg:
			if y[1] % x[1] == 0 and z[1] % x[1] == 0 and z[1] % y[1] == 0:
				print x,
				print y,
				print z

