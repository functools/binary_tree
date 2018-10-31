import gc
class Node:

	def __init__(self, value, father = None, right_child = None):
		self.value = value
		self.father = father
		self.left_child = None	
		self.right_child = right_child	
		self.go_left = False
		gc.enable()
	def __repr__(self):
		return self.value
	def set_left(self, state):
		self.go_left = state		
	def get_left(self):
		return self.go_left
	def getvalue(self):
		return self.value
	def depth(self):
		counter = 0
		temp = self.father
		while (temp is not None):
			counter += 1
			temp = temp.father
		return counter

class binary_tree:
	def getroot(self):
		return self.root
	def add(self, value, father = None):
		if (self.root is None):
			self.root = Node(value)
			return None
		if (father is None):
			print(value)
			return None
		if (father.left_child is None):
			father.left_child = Node(value, father = father, right_child = father)
			return None
		if ((father.right_child is None) or (father.right_child.father != father)):
			father.right_child = Node(value, father = father, right_child = father.right_child)	
	def remove(self, node):
		if (node == None):
			return None	
		if (node == self.root):
			self.root = None
			gc.collect()	
			return None
