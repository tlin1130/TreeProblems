
# Simple Node class used to construct BST
class Node:

	def __init__(self, key):
		self.value = key
		self.left = None
		self.right = None
		
# Return True if given binary tree is balanced; otherwise, return False
# A binary tree is balanced the difference of depths of any two leaf nodes is <= 1
def is_balanced(root):

	if root == None:
		return True

	depths = []
	stack = []
	stack.append((root,0))

	while len(stack) != 0:

		node = stack.pop()

		# node if a leaf
		if (node[0].left == None) and (node[0].right == None):

			if node[1] not in depths:
				depths.append(node[1])

			if len(depths) > 2 or (len(depths) == 2 and abs(depths[0] - depths[1]) > 1):
				return False

		# node is not a leaf
		else:

			if node[0].right is not None:
				stack.append((node[0].right, node[1] + 1))
			if node[0].left is not None:
				stack.append((node[0].left, node[1] + 1))

	return True

# test code
root = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
print is_balanced(root)
# output = True
node5 = Node(5)
node4.left = node5
print is_balanced(root)
# output = False
