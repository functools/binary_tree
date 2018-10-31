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
	if ((node.left_child is None) and ((node.right_child == None) or (node.right_child == node.father) 
			or (node.right_child.father != node))):
			if (node == node.father.left_child):
				node.father.left_child = None		
			else:
				node.father.right_child = node.right_child
			return None	
		if (node == node.father.left_child):
				node.father.left_child = None
		else:
			temp_node = node
			while (temp_node.right_child is not None):
				if (temp_node.right_child.father is not temp_node):
					temp_node = temp_node.right_child
					break
				temp_node = temp_node.right_child			
			node.father.right_child = None if temp_node.right_child == None else temp_node	
		gc.collect()
		
	def print(self):
		temp_node = self.root
		while (temp_node is not None):
			if ((temp_node.left_child is not None) and (temp_node.get_left() == False)):
				temp_node.set_left(True)
				temp_node = temp_node.left_child
			else:
				print(temp_node.getvalue())
				temp_node.set_left(False)
				temp_node = temp_node.right_child		
