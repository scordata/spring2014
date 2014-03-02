"""
Adam Najman
Cyrptography
Problem Set 1
Quesiton 6

REQUIRES PYTHON 3 FOR ICELANDIC SUPPORT

This operates by building a confidence interval,
measuring the average of the best frequencies and
replacing it if we find a better value for all
32 rotations. This does not assume that the Vigenere table
has been scrambled. 

"""
from collections import Counter 
from operator import itemgetter
import collections

alphabet = 'aábdðeéfghiíjklmnoóprstuúvxyýþæö'
print (alphabet)
temp = [(alphabet * 2)[x:x+32] for x in range(32)]
table = '\n'.join(temp)
print (table)



# After frequency analysis, it shows the key is:
# ersvkndöpafð
# We will use these strings to decode
v1 = 'eéfghiíjklmnoóprstuúvxyýþæöaábdð'
v2 = 'rstuúvxyýþæöaábdðeéfghiíjklmnoóp'
v3 = 'stuúvxyýþæöaábdðeéfghiíjklmnoópr'
v4 = 'vxyýþæöaábdðeéfghiíjklmnoóprstuú'
v5 = 'klmnoóprstuúvxyýþæöaábdðeéfghiíj'
v6 = 'noóprstuúvxyýþæöaábdðeéfghiíjklm'
v7 = 'dðeéfghiíjklmnoóprstuúvxyýþæöaáb'
v8 = 'öaábdðeéfghiíjklmnoóprstuúvxyýþæ'
v9 = 'prstuúvxyýþæöaábdðeéfghiíjklmnoó'
v10= 'aábdðeéfghiíjklmnoóprstuúvxyýþæö'
v11= 'fghiíjklmnoóprstuúvxyýþæöaábdðeé'
v12= 'ðeéfghiíjklmnoóprstuúvxyýþæöaábd'


t1 = str.maketrans(v1, alphabet)
t2 = str.maketrans(v2, alphabet)
t3 = str.maketrans(v3, alphabet)
t4 = str.maketrans(v4, alphabet)
t5 = str.maketrans(v5, alphabet)
t6 = str.maketrans(v6, alphabet)
t7 = str.maketrans(v7, alphabet)
t8 = str.maketrans(v8, alphabet)
t9 = str.maketrans(v9, alphabet)
t10 = str.maketrans(v10, alphabet)
t11 = str.maketrans(v11, alphabet)
t12 = str.maketrans(v12, alphabet)



# Our cypher text
foo = 'hóóvskirafsípránxraatóóhrlóáæpdéuaýþmdxajröðéábiðhjéurkmýæóðætúrævsöáúáóðhöþsgeéjyönj\
glheþdaouhxyaxeóéoóímýæsðsóýlþævlfðsúðhkhpnþeóémgffjrhxnóórskrmíýjéuúeóeæuðutdýenry\
úötöúllæöaxárymröþxdáujxerílivexxöúoþlæyöxvýóavtelébvdsaexfmæétyksbnpkfðvóýlsképnajvlr\
óolraújtðidgnxenrtúhshspgaruykóækiðétauaelliaabðyueýmævmvhæaéáóeeebýuaevxsrnýxpkbbþx\
yóaóetóxvgpptyksbnpkfðbýýhhnyövhoéduddxaktapþentiöenhkyihtíæsxrýsöþnvdsðjybúínvfnúnýfi\
vbðöþfxserívpirxbýýaehelexýburkmýæehjélðötégðxnvkgjkiæölafxáéáráafyóbgökbmeerællúvixvx\
bgfeömiósxrýuvsþexkýævdajáýmðfvdþieðdaéxaíörsk'

# A function to count occurences of
# letters in a string, then sorts by
# result
def stat(foo, pnt=False):
  ca = Counter(foo)
  if pnt:
    print (ca)
  avg = []
  for x in ca:
        avg.append([x, ca[x]/(len(foo)/100.0)])  
        #avg.append([x, ca[x]/5.77])
  if pnt:
    print (sorted(avg, key=itemgetter(1), reverse=True))
  return sorted(avg, key=itemgetter(1), reverse=True)

# Show the whole string
stat(foo)
# Looks like it's polyalphabetic


# Frequencies of decoded larger text
comp = [ ['r', 9.1], ['a', 9.1], ['i', 7.9], ['n', 7.8], ['e', 5.9], ['s', 5.1], ['g', 4.9], ['u', 4.8],
         ['l', 4.7], ['ð', 4.7], ['t', 4.2], ['m', 3.6], ['o', 3.0], ['þ', 2.9], ['h', 2.8], ['k', 2.6], 
         ['v', 2.5], ['f', 2.4], ['á', 1.7], ['d', 1.4], ['í', 1.2], ['j', 1.1], ['ó', 1.1], ['ú', 0.9], 
         ['ö', 0.8], ['b', 0.8], ['æ', 0.7], ['é', 0.7], ['y', 0.7], ['p', 0.6], ['ý', 0.1], ['x', 0.0] ]

print (comp)

# This loops builds a confidence interval for determining the key length
# We start at last = 10. We compute the average distance in the frequencies
# for the first 5 values. If that value gets smaller, we have a better
# confidence value. This happens 32 times, since that's the maximum amout
# of rotations you'll get in this language.
last = 10
for i in range(33):
  temp = foo[i:len(foo):i+1]
  bar = stat(temp)
  litmus = ( abs( bar[0][1] - comp[0][1] ) + abs( bar[1][1] + comp[1][1] )\
           + abs( bar[2][1] - comp[2][1] ) + abs( bar[3][1] - comp[3][1] ) + abs( bar[4][1] - comp[4][1])) 
  litmus = float(litmus) // 5.0
  print ("last is: %i" % last)
  print ("litmus is: %i" % litmus)
  if last >= litmus:
    last = litmus
    print ("MATCH FOUND AT: %i" % i)
    print ("%i: " % i,)
    print (bar[0][1], comp[0][1]),
    print (bar[1][1], comp[1][1]),
    print (bar[2][1], comp[2][1]),
    print (bar[3][1], comp[3][1]),
    print (bar[4][1], comp[4][1])



# Confedence intervals shows that
# the most likley key length is
# 12. The distribution produced
# have finished converging with icelandic.

k0 = foo[0:len(foo):12]
k1 = foo[1:len(foo):12]
k2 = foo[2:len(foo):12]
k3 = foo[3:len(foo):12]
k4 = foo[4:len(foo):12]
k5 = foo[5:len(foo):12]
k6 = foo[6:len(foo):12]
k7 = foo[7:len(foo):12]
k8 = foo[8:len(foo):12]
k9 = foo[9:len(foo):12]
k10 = foo[10:len(foo):12]
k11 = foo[11:len(foo):12]


# This section is to make sure
# I've got my math right
# And divided up the string properly
"""
print (k0)
print (len(k0))
print (k1)
print (len(k1))
print (k2)
print (len(k2))
print (k3)
print (len(k3))
print (k4)
print (len(k4))
print (k5)
print (len(k5))
print (k6)
print (len(k6))
print (k7)
print (len(k7))
print (k8)
print (len(k8))
print (k9)
print (len(k9))
print (k10)
print (len(k10))
print (k11)
print (len(k11))


x = len(k0) + len(k1) + len(k2) + len(k3) + len(k4) + len(k5) + \
    len(k6) + len(k7) + len(k8) + len(k9) + len(k10) + len(k11)

print (x)
"""

# Here we see the analysis of
# each substring
"""
print ("k0 analisys")
stat(k0, True)
print ("k1 analisys ")
stat(k1, True)
print ("k2 analisys ")
stat(k2, True)
print ("k3 analisys ")
stat(k3, True)
print ("k4 analisys ")
stat(k4, True)
print ("k5 analisys ")
stat(k5, True)
print ("k6 analisys ")
stat(k6, True)
print ("k7 analisys ")
stat(k7, True)
print ("k8 analisys ")
stat(k8, True)
print ("k9 analisys ")
stat(k9, True)
print ("k10 analisys ")
stat(k10, True)
print ("k11 analisys ")
stat(k11, True)
"""


# This loop decodes each part of the substring
# and builds it back into a readable format
# (without spaces...)
retval = ''
k0 = k0.translate(t1)
k1 = k1.translate(t2)
k2 = k2.translate(t3)
k3 = k3.translate(t4)
k4 = k4.translate(t5)
k5 = k5.translate(t6)
k6 = k6.translate(t7)
k7 = k7.translate(t8)
k8 = k8.translate(t9)
k9 = k9.translate(t10)
k10 = k10.translate(t11)
k11 = k11.translate(t10)



for i in range(len(t1)):
  retval += k0[i]
  retval += k1[i]
  retval += k2[i]
  retval += k3[i]
  retval += k4[i]
  retval += k5[i]
  retval += k6[i]
  retval += k7[i]
  retval += k8[i]
  retval += k9[i]
  retval += k10[i]
  retval += k11[i]


retval += k0[-1]
retval += k1[-1]
retval += k2[-1]
retval += k3[-1]


print (retval)

"""
OUTPUT:
ðæþagþfskflílajukðþádóíhmxþgodafðasþimeföðýepáyiösukiðinhæíðvbdyohóal
úxóösiðgúbfvyúnfrvnúkaáæubxtjejetlpúmsænnavmæxöélaðnðmnavnoieíéirólöð
éyþóírnvötæjhfðúæóaibíiéaþónkypíáéíæíöjapámfxyókuðluexaatsþhbyföooúxh
bóitþöaótaxohjpóáóxamvóábaeöoakaðræfsgþdrþaevhaþúáðþvvtþiæryáúaouehlh
nöpfffúlöæéiöóáfinbmyivaþnéæújjöémóhvjogesbémýnaaeeýfavyakybúéévpbbuö
xóglöábaeöoakaðþgfnýaúaéhiéædlikniukptexaar
"""
