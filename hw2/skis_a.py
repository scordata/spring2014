"""
Adam Najman
HomwWork2
skis_a.py
"""
#Answer placeholder
answer = 0

#Target number and options to
#choose from
target = 5
options = [1,2,1,4,3,1,3]

#Dictionary/hash to hold values
ht = {}

#For loop to prime the hash
for x in options:
  if x in ht:
    ht[x] = 1 + ht[x]
  else:
    ht[x] = 1

#For every value in ht
for y in ht:
  #Find the compliment
  z = target - y
  #If the compliment exists in enough quantity
  if z in ht and (ht[z] > 0 and ht[y] > 0):
    #Adjust the values and increment answer
    ht[z] -= 1
    ht[y] -= 1
    answer += 1

print answer


