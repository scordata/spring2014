"""
Adam Najman
Homework#2
skis_b.py
"""
#Placeholder for answer
answer = 0

#Our target number of pairs
target = 5
#Options to select from
options = [1,2,1,4,3,1,3]

#Start and end pointers
start = 0
end = len(options) - 1


while(start < end):
  #If the end points are smaller than target
  if options[start] + options[end] < target:
    #Increment the first pointer
    start += 1
  #If the end points are bigger than the target
  elif options[start] + options[end] > target:
    #Decrement the last pointer
    end -= 1
  #If we have a suitable answer...
  else:
    #Increment answer and close the pointer gap
    start += 1
    end -= 1
    answer += 1

print answer
