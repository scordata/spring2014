

f = open("lisin.txt",'r')
o = open("lisout.txt", 'w')

ops = []
retVal = []

for line in f:
  print line
  ops.append(map(str ,line.split()))

print "ops is:", ops


for elem in ops:
  temp = max( [retVal[j] for j in elem \
              if retVal[j][-1] < elem] or [[]] , key=len) \
              + [ops[elem]] 
  print "temp is: ", temp
  retVal.append(temp)

