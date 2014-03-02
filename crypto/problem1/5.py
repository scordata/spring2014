"""
Adam Najman
Cyrptography
Problem Set 1
Quesiton 5
"""
from collections import Counter 
from operator import itemgetter
from string import maketrans

alphabet = 'abcdefghijklmnopqrstuvwxyz'

# After frequency analysis, it shows the key is:
# MZEJBL
# We will use these strings to decode
vM = 'mnopqrstuvwxyzabcdefghijkl'
vZ = 'zabcdefghijklmnopqrstuvwxy'
vE = 'efghijklmnopqrstuvwxyzabcd'
vJ = 'jklmnopqrstuvwxyzabcdefghi'
vB = 'bcdefghijklmnopqrstuvwxyza'
vL = 'lmnopqrstuvwxyzabcdefghijk'

t1 = maketrans(vM, alphabet)
t2 = maketrans(vZ, alphabet)
t3 = maketrans(vE, alphabet)
t4 = maketrans(vJ, alphabet)
t5 = maketrans(vB, alphabet)
t6 = maketrans(vL, alphabet)
# Our cypher text
foo = 'sqmvwtezknehmqljusenscippgmblcumouforqswulzcrxxtzrxnboaeqxvyfhrpcldaimteqdhbuzrqmpie\
fgibpfxrsogpmqjdmlpuiatldhibipoztnsdzhqkmjumeubokrgqbxndvcpetdpjtnuumxvdbkijttzfsobwgs\
ikveusljulymsctsmoimgzdrtxseuuicstojwwpcyzhnuzonyaulzzqxszgrpxpvumkpmlermcilfzqavoqkc\
bulyoimbypvewuwauibnlvdwczearxavendjxspmvewuzzzqkmtzfrhnathxqbemlgdsemhpnezrslrtqm\
hvyszbnvcjzzblnbeqcsogpmsyafmkcmbtpyaprorzzxdsppdjxsxqcywgtzhwqfoedrccprnvnnjfhqnjyf\
nxqjdnqijusumkfpcxcwlbcodljmqyzhnvammhcilfrsubxqkcjoogmjjtsunrjcwqsljuoafwkbcwzxvfle\
hljmenxxqfxigcrjyfgmbxpmjtrqtzfxrnpaetnbnqgeefyaciujrtsxxqlerefbjfgicjxq'

# A function to count occurences of
# letters in a string, then sorts by
# result
def stat(foo):
  ca = Counter(foo)
  print ca
  avg = []
  for x in ca:
        avg.append([x, ca[x]/(len(foo)/100.0)])
  	#avg.append([x, ca[x]/5.77])
  print sorted(avg, key=itemgetter(1), reverse=True)

# Show the whole string
stat(foo)
# Looks like it's polyalphabetic

# Trial and error shows that
# the most likley key length is
# 6. The distribution produced
# most closely matches English.
# To make more sets, add:
# kx = foo[x:len(foo):y]
# where y = step size (number of sets)
# and x is the set number.
# Removing sets is the same.
k0 = foo[0:len(foo):6]
k1 = foo[1:len(foo):6]
k2 = foo[2:len(foo):6]
k3 = foo[3:len(foo):6]
k4 = foo[4:len(foo):6]
k5 = foo[5:len(foo):6]


# This section is to make sure
# I've got my math right
# And divided up the string properly
"""
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

x = len(k0) + len(k1) + len(k2) + len(k3) + len(k4) + len(k5)
print x
"""

# Here we see the analysis of
# each substring
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


# This loop decodes each part of the substring
# and builds it back into a readable format
# (without spaces...)
retval = ''
for i in range(len(k1)):
  retval += k0.translate(t1)[i]
  retval += k1.translate(t2)[i]
  retval += k2.translate(t3)[i]
  retval += k3.translate(t4)[i]
  retval += k4.translate(t5)[i]
  retval += k5.translate(t6)[i]

retval += k0.translate(t1)[-1]
"""  
print k0.translate(t1)
print k1.translate(t2)
print k2.translate(t3)
print k3.translate(t4)
print k4.translate(t5)
print k5.translate(t6)
"""
print retval


"""
After Shifting and translating:
grimvisagedwarhathsoothedhiskrinkledfrontandnowinsteadofmountingbarbe
dsteedstofrightthesoulsoffearfuladversarieshecapersnimblyinaladyschamber
tothelasciviouspleasingofalutebutithatamnotshapedforsportivetricksnormad
etocourtanamorouslookingglassithatamrudelystampedandwantlovesmajestytost
rutbeforeawantonamblingnymphithatamcurtailedofthisfairproportioncheatedo
ffeaturebydissemblingnaturedeformedunfinishedsentbeforemytimeintothisbre
athingworldscarcehalfmadeupandthatsolamelyandunfashionablethatdogsbarkat
measihaltbythemwhyiinthisweakpipingtimeofpeacehavenodelighttopassawaythe
time
"""
