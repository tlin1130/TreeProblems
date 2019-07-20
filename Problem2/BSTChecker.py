import sys

# Simple Node class used to construct BST
class Node:

	def __init__(self, key):
		self.value = key
		self.left = None
		self.right = None

# Check if a given binary tree is a valid BST
def checkBST(root):

	n = root
	stack = []
	stack.append([n, -sys.maxint - 1, sys.maxint])

	while (len(stack) > 0):

		node = stack.pop()

		# check if value in range
		value = node[0].value
		if not (value <= node[2] and value >= node[1]):
			return False

		# value in range
		# push children onto stack
		if node[0].right:
			stack.append([node[0].right, node[0].value, node[2]])
		if node[0].left:
			stack.append([node[0].left, node[1], node[0].value])

	return True

# test code
node0 = Node(20)
node1 = Node(10)
node2 = Node(35)
node3 = Node(5)
node4 = Node(30)
node0.left = node1
node0.right = node2
node1.left = node3
node1.right = node4
print checkBST(node0)
# output = False

node4.value = 12
print checkBST(node0)
# output = True

node5 = Node(19)
node6 = Node(36)
node2.left = node5
node2.right = node6
print checkBST(node0)
# output = False
