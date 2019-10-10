# Python3 program to find the mirror node in 
# Binary tree 
raw_input = """ 7 3 2
                2 3 R
                2 4 L
                3 5 R
                3 6 L
                4 7 R
                4 8 L
                5 9 L
                7
                9
                2 """
raw_input = (i for i in map(lambda x: x.strip(), raw_input.split('\n')))
class Node: 
	'''A binary tree node has data, reference to left child 
		and a reference to right child '''

	def __init__(self, key, lchild=None, rchild=None): 
		self.key = key 
		self.lchild = None
		self.rchild = None

def formNodes(data, root):
  L = R = False
  for i in range(len(data)):
    perent, child, side = data[i].values()
    if perent==root.key:
      if side=='L':
        root.lchild = formNodes(data[:i]+data[i+1:], Node(child))
        L = True
      elif side=='R':
        root.rchild = formNodes(data[:i]+data[i+1:], Node(child))
        R = True
    if L and R:
      break
  return root
        
# recursive function to find mirror 
def findMirrorRec(target, left, right): 

	# If any of the node is none then node itself 
	# and decendent have no mirror, so return 
	# none, no need to further explore! 
	if left == None or right == None: 
		return None

	# if left node is target node, then return 
	# right's key (that is mirror) and vice versa 
	if left.key == target: 
		return right.key 
	if right.key == target: 
		return left.key 

	# first recur external nodes 
	mirror_val = findMirrorRec(target, left.lchild, right.rchild) 
	if mirror_val != None: 
		return mirror_val 

	# if no mirror found, recur internal nodes 
	return findMirrorRec(target, left.rchild, right.lchild) 

# interface for mirror search 
def findMirror(root, target): 
	if root == None: 
		return None

	if root.key == target: 
		return target 

	return findMirrorRec(target, root.lchild, root.rchild) 

  
N, Q, X = map(int, next(raw_input).split())
data = [dict(zip(['perent','child','side'], next(raw_input).split()))for i in range(N)]
root = formNodes(data, Node(str(X)))
for _ in range(Q):
  mirror = findMirror(root, next(raw_input))
  print(mirror if mirror else 'Not Exist')
