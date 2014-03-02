import sys
sys.setrecursionlimit(1000000)

def _fibo(n, cache):
  if n in cache:
    return cache[n]
  cache[n] = 1 if n < 2 else _fibo(n-1, cache) + _fibo(n-2, cache)
  return cache[n]

def fib(n):
    return _fibo(n, cache=[])

print fib(4000000)
