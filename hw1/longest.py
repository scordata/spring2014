"""
Adam Najman
HW#1
longest.py
LAST EDITED: 2/4/14
"""

"""
Sort function from slides
"""
def sort(a):
  if a == []:
    return []
  else:
    pivot = a[0]
    left = [x for x in a if x < pivot ]
    right = [ x for x in a[1:] if x >= pivot]
    return [sort(left)] + [pivot] + [sort(right)]


"""
The longest path within a binary
tree is known as the diameter.
This finds the amount of nodes the
diameter has

This runs in O(n^2)
I'm working on squeezing the
depth calculation into each
recursive step without
calling the helper function
"""
def diameter(tree, memo = [], retVal = {}):
  
 # print tree

  #upon reaching a leaf
  #or calling on empty tree
  if tree == []:
    #print "Hit leaf"
    return 0

  #find hight of left and right
  #subtrees
  leftDepth = depth(tree[0])
  rightDepth = depth(tree[2]) 

  #call diameter on the left
  #and right subtrees
  leftDiameter = diameter(tree[0])
  rightDiameter = diameter(tree[2])

  #memoize node values:
  # [Node name, Depth of left subtree,
  # Depth of right subtree, left diameter,
  # right diameter
  if tree != []:
    memo.append([tree[1], leftDepth, rightDepth, \
                leftDiameter, rightDiameter])


#  print "memo is: ",
#  print memo
#
#  print "leftDepth is: ", 
#  print  leftDepth
#  print "rightDepth is: ",
#  print  rightDepth
#
#  print "leftDiameter is: ",
#  print  leftDiameter
#  print "rightDiameter is: ",
#  print  rightDiameter


  #dict to compute values for displaying longest
  #path. formula is:
  # max(left diameter, right diameter, 
  #     (left depth + right depth) )
  
  retVal[tree[1]] = max(memo[-1][3],\
                        memo[-1][4],\
                        memo[-1][1] + \
                        memo[-1][2]  \
                        )
  
  # I'm having trouble comparing the 
  #values in the dict to determine the
  #path for printing
  # Wish I had more time.
  print "diameter is: ",
  print retVal
 
    

  return max( 1 + leftDepth + rightDepth , \
         max( leftDiameter, rightDiameter)) - 1


"""
A helper function to find
the depth of a (sub)tree.
Used to calculate diameter
"""
def depth(tree):

  #Base case
  if tree == []:
    #print "hit Leaf"
    return 0

  #Recursive struture navigation
  #Adds one every level to calculate depth
  return 1 + max(depth(tree[0]), depth(tree[2]))

def test(tree, level = 0, cval = 0, retVal = []):
  if tree == []:
    level += 1
    print "hit leaf"
    print level
    return

  cval = tree[1]
  print "cval is %d" % cval
  retVal.append(cval)
  print "retVal is: "
  print retVal
  
  level -= 1
  print "level is %d" % level
  test(tree[0])
  test(tree[2])

def test2(tree, path = []):

  leftSub = depth(tree[0])
  rightSub = depth(tree[2])
  rootDepth = depth(tree[1])

  print "leftSub is: %i" % leftSub
  print "rightSub is: %i" % rightSub
  print "rootDepth is %i" % rootDepth


if __name__ == "__main__":
  foo = [4,2,6,3,5,7,1,9]
  print "unsorted list:"
  print foo
  foo = sort(foo)
  print "sorted list:"
  print foo
  print "length of path is: %i" % diameter(foo)
