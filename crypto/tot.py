import fractions

def phi(n):
  amount = 0

  for k in range(1, n + 1):
     if fractions.gcd(n, k) == 1:
        amount += 1
  return amount
"""
for i in range(10000):
  if 110 == phi(i):
    print "found: ",
    print i
"""
print phi(1)
print phi(2)
print phi (5)
print phi(10)
print phi(11)
print phi (22)
print phi(55)
print phi(110)
print phi (121)
print phi(242)

print "------"
print phi(3)
print phi(6)
print phi(7)
print phi(14)
print phi(35)
print phi(70)
print phi(101)
print phi(202)
