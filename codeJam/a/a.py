"""
Google Code Jam
Problem A small
Adam Najman

"""



input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')

working_set = []


def comp(a, b, l1, l2):
  count = 0
  match = 0
  first = l1[a]
  second = l2[b]
  for x in first:
    for y in second:
      if x == y:
        count += 1
        match = x

  #print "count is: ", count
  #print "match is: ", match
  return match, count



for line in input_file:
  l = line.strip()
  working_set.append(map( int, l.split(' ')))

tests = int(working_set[0][0])

for x in xrange(tests):
  orig_config = []
  new_config = []
  a = working_set[ (x*10) + 1 ][0] - 1
  b = working_set[ (x*10) + 6 ][0] - 1
  #print "a is: ", a
  #print "b is: ", b
  for i in xrange(4):
    orig_config.append(working_set[(x*10) + (i+2)])
    new_config.append(working_set[(x*10) + (i+7)])
  result, count = comp(a, b, orig_config, new_config) 

  if count == 0:
    print "Case #%i: Volunteer cheated!" % int(x+1)
    output_file.write("Case #%i: Volunteer cheated!\n" % int(x+1))
  if count == 1:
    print "Case #%i: %i" % (int(x+1) , result)
    output_file.write("Case #%i: %i\n" % (int(x+1) , result))
  if count > 1:
    print "Case #%i: Bad magician!" % int(x+1)
    output_file.write("Case #%i: Bad magician!\n" % int(x+1))
