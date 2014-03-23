from itertools import groupby
 
maxwt = 3
 
groupeditems = (
            ("socks", 2, 4, 2),
            ("book", 3, 5, 3),
           )
items = sum( ([(item, wt, val)]*n for item,
            wt, val,n in groupeditems), [])
 
print "items is: "
print items

def knapsack01_dp(items, limit):
    table = [[0 for w in range(limit + 1)] 
          for j in xrange(len(items) + 1)]

    for j in xrange(1, len(items) + 1):
        item, wt, val = items[j-1]
        for w in xrange(1, limit + 1):
            if wt > w:
                table[j][w] = table[j-1][w]
            else:
                table[j][w] = max(table[j-1][w],
                                  table[j-1][w-wt] + val)
 
    result = []
    w = limit
    for j in range(len(items), 0, -1):
        was_added = table[j][w] != table[j-1][w]
 
        if was_added:
            item, wt, val = items[j-1]
            result.append(items[j-1])
            w -= wt
 
    return result
 
 
bagged = knapsack01_dp(items, maxwt)
print("Bagged the following %i items\n  " % len(bagged) +
      '\n  '.join('%i off: %s' % (len(list(grp)), item[0])
                  for item,grp in groupby(sorted(bagged))))
print("for a total value of %i and a total weight of %i" % (
    sum(item[2] for item in bagged), sum(item[1] for item in bagged)))
