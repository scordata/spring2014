import crypt

print "encrypting egg with salt HX"

foo = crypt.crypt("a", "HX")

print "checking for vuln"

bar = 0
memo = {}

while (True):
  bar += 1
  memo[bar] = foo
  if foo == "HXegg":
    break
  if foo in memo:
    print "found a reuse! " + foo + " after " + str(bar) + " attempts!\n"
  if bar % 100000 == 0:
    print "after " + str(bar) + " attempts, foo is: " + foo +"\n"
  foo = crypt.crypt(foo, "HX")

print "Found vuln, took " + bar + "attempts"
