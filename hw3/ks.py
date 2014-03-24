items = [
	["map",		2,	4,	2],
	["compass",	3,	5,	3]
	]
 
#cache: could just use memoize module, but explicit caching is clearer
def choose_item(weight, idx, cache):
    print "considering the following: "
    print items[idx]
    if idx < 0: return 0, [0]
 
    k = (weight, idx)
    if k in cache: return cache[k]
 
    name, w, v, qty = items[idx]
    best_v, best_list = 0, [0]
 
    for i in range(0, qty + 1):
        wlim = weight - i * w
        if wlim < 0: break
 
        val, taken = choose_item(wlim, idx - 1, cache)
        if val + i * v > best_v:
            best_v = val + i * v
            best_list = taken[:]
            best_list.append(i)
 
    cache[k] = [best_v, best_list]
    print "cache[k] is: " , cache[k]
    return best_v, best_list
 
print "items is: "
print items
v, lst = choose_item(3, len(items) - 1, {})
print "v is: ", v
print "lst is: "
print lst
w = 0
for i, cnt in enumerate(lst):
    if cnt > 0:
        print cnt, items[i][0]
        w = w + items[i][1] * cnt
 
print "Total weight:", w, "Value:", v
