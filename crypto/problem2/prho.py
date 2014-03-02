import random
import fractions

def fermat(n):
  return (2**(2**n)) + 1

def r(x,n):
  return (x**2 + random.randint(0,10000) ) % n

def gcd(a, b):
  while b:
    a, b = b, a % b
  return a
   
def pollard_rho(n, s, f):
  x = y = s
  d = 1
  while d == 1:
    x = f(x, n)
    y = f(f(y, n), n)
    d = gcd(abs(y - x), n)
  return d
     
n = fermat(6)
print n
s = 2
f = lambda x, m: (x**2 + 2) % m
     
print pollard_rho(n, s, f)
