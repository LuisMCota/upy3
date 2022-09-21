class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def traversePreOrder(self):
        print(self.val, end=' ')
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()

    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.val, end=' ')
        if self.right:
            self.right.traverseInOrder()

    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.val, end=' ')


root = Node('A')

root.left = Node('B')
root.right = Node('C')

root.left.left = Node('D')
root.right.right = Node('F')

root.left.left.left = Node('E')
root.right.right.right = Node('G')

root.left.left.left.left = Node('H')
root.right.right.right.right = Node('L')

root.left.left.left.left.left = Node('I')
root.right.right.right.right.right = Node('M')

root.left.left.left.left.left.left = Node('J')
root.right.right.right.right.right.right = Node('N')

root.left.left.left.left.left.left.left = Node('K')
root.right.right.right.right.right.right.right = Node('O')


print("Pre order Traversal: ", end="")
root.traversePreOrder()
print("\nIn order Traversal: ", end="")
root.traverseInOrder()
print("\nPost order Traversal: ", end="")
root.traversePostOrder()