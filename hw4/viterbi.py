
from collections import defaultdict
from collections import Counter

f = open('input.txt', 'r')
o = open('output.txt', 'w')

num_graphs =  int(f.readline())


for times in xrange(num_graphs):
  path = 0
  temp = defaultdict(int)
  topograph = []
  line, line2 = f.readline(), f.readline()
  nodes, edges = int(line[0]), int(line[2])
  graph = [(int(line2[x+1]), int(line2[x+4])) for x, y in \
            enumerate(line2) if y == '(']
  #graph2 = [edge[1] for edge in graph]
  start, end = graph[0][0], nodes #graph[-1][0]
  print "nodes, edges: ", nodes, edges
  print "connections: ", line2 
  print "graph: ", graph
  #print "graph2: ", graph2
  print "start node, end node: ", start, end
  #print "Indegree list : " , Counter(graph2)
  for x in xrange(edges):
    temp[graph[x][0]]
    temp[graph[x][1]] += 1
  print "temp is: ", temp
  for v in temp:
    foo = min(temp, key=temp.get)
    #print "min temp is: ", foo
    topograph.append([foo])
    temp[foo] = float('inf')
    for z in graph:
      if z[0] == foo:
        if foo == end:
          #print "---------------------"
          break
        #print "con found: " , z
        temp[z[1]] -= 1
        path += 1
    #print "new temp: ", temp
    #print "path : ", path
  #if start not in temp:
  #  print "start node has indegree of 0"
  print "toposort was: ", topograph
  """
  matrix = [[0 for y in xrange(len(graph) + 1)] \
               for x in xrange(len(graph) + 1)]
  for elem in graph:
    matrix[elem[0]][elem[1]] = 1
  print "matrix: "
  for thing in matrix:
    print thing
  paths = []
  numpaths = 0
  for i in xrange(1, len(graph) + 1):
    if matrix[i][nodes] == 1:
      paths.append(i)
      numpaths += 1
  print paths
  print numpaths
  for j, h in enumerate(paths):
    print j, h
    if matrix[j][h] == 1:
      paths.append(j)
      print "HIT!", j, h
      numpaths += 1
  print paths
  print numpaths
  """
