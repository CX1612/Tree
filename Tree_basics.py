# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")

print("We have made it")

class BinaryTree:
    def __init__(self,value):
        self.value = value
        self.right_node = None
        self.left_node = None

    def insert_left(self, value):
        if self.left_node == None:
            self.left_node = BinaryTree(value)
        else:
            new_Node = BinaryTree(value)
            new_Node.left_node = self.left_Node
            self.left_Node = new_Node
            
    def insert_right(self, value):
        if self.right_node == None:
            self.right_node = BinaryTree(value)
        else:
            new_Node = BinaryTree(value)
            new_Node.right_node = self.right_node
            self.right_node = new_Node
        
a_node = BinaryTree('a')
a_node.insert_left('b')
a_node.insert_right('c')
print(a_node.value)
print(a_node.left_node.value)
print(a_node.right_node.value)

b_node = a_node.left_node
b_node.insert_right('d')
b_node.insert_left('meow')
c_node = a_node.right_node
c_node.insert_left('e')
c_node.insert_right('f')

print(a_node.value)
print(a_node.left_node.value)
print(a_node.right_node.value)
print(b_node.value)
print(b_node.left_node.value)
print(b_node.right_node.value)
print(c_node.value)
print(c_node.left_node.value)
print(c_node.right_node.value)