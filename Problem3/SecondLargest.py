# Simple Node class used to construct BST
class Node:

	def __init__(self, key):
		self.value = key
		self.left = None
		self.right = None

# Give root and size of a BST, the function returns the second largest item in BST
def find_2nd_largest_item(root, size):

	if (size < 2):
		return 'Less than 2 items'

	if (root.right != None):

		cur = root
		prev = root.left

		while (cur.right != None):
			prev = cur
			cur = cur.right

		if (cur.left == None):
			return prev.value
		else :
			cur = cur.left
			while (cur.right != None):
				cur = cur.right
			return cur.value

	else:

		cur = root.left

		while (cur.right != None):
			cur = cur.right

		return cur.value

# test code
# construct BSTs manually
# BST1
root = Node(20)
node1 = Node(25)
node2 = Node(18)
root.right = node1
root.left = node2
node3 = Node(19)
node4 = Node(14)
node2.right = node3
node2.left = node4
node5 = Node(30)
node6 = Node(21)
node1.right = node5
node1.left = node6
node7 = Node(32)
node8 = Node(28)
node5.right = node7
node5.left = node8
size = 9

result = find_2nd_largest_item(root, size)
print result
# output = 30

# BST2
root = Node(20)
size = 1

result = find_2nd_largest_item(root, size)
print result
# output = 'Less than 2 items'

# BST3
root = Node(20)
node1 = Node(25)
node2 = Node(15)
node3 = Node(16)
node4 = Node(17)
node5 = Node(13)
#root.right = node1
root.left = node2
node2.left = node5
node2.right = node3
node3.right = node4
size = 6

result = find_2nd_largest_item(root, size)
print result
# output = 17
