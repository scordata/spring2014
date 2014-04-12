"""
Google Code Jam
Problem b
Adam Najman
"""


i = open('input.txt', 'r')
o = open('output.txt', 'w')


tests = int(i.next())

print tests

done = False
times = 1

for line in i:
  l = line.strip()
  print l
  farm_price, farm_max, goal = map(float, l.split(' '))
  print "farm_price, farm_max, goal: ", farm_price, farm_max, goal

  base = 2 #cps

  farms = 0
  total_running_time = 0.0
  while(not done):
    total_cps = base + (farms * farm_max)
    #print "total_cps: ", total_cps

    farm_purchase_rate = (farm_price / total_cps)
    #print "farm_purchase_rate: ", farm_purchase_rate

    cps_update = base + ((farms + 1.0) * farm_max)
    #print "cps if we buy another farm: " , cps_update
    goal_update = goal / cps_update
    #print "goal time with new farm: " , goal_update
  
    time = goal / total_cps
    #print "time: ", time

    #time_for_farm = farm_purchase_rate / cps_update
    #print "time to buy farm = ",  time_for_farm


    if( time > (farm_purchase_rate + goal_update)):
      #print "we should buy a farm"
      total_running_time += farm_purchase_rate
      #print "yes ", total_running_time
      farms += 1
    else:
      #print "we should not buy a farm"
      total_running_time += time
      done = True
  #print "for solution ", times, "we should buy " , farms, " farms"
  #print "this took " , total_running_time, " seconds"
  print "Case #%i: %f\n" % (times, total_running_time)
  o.write("Case #%i: %f\n" % (times, total_running_time))
  times += 1
  done = False
