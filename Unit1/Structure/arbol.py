class Node:
    def _init_(self, word):
        self.leftside = None
        self.rightside = None
        self.word = word
 
def insert(root, word):
    if root is None:
        return Node(word)
    else:
        if root.word == word:
            return root
        elif root.word < word:
            root.rightside = insert(root.right, word)
        else:
            root.leftside = insert(root.left, word)
    return root

 
def ordered_insert(root):
    if root:
        ordered_insert(root.left)
        print(root.word)
        ordered_insert(root.right)
 

 
r = Node('A')
r = insert(r, 'B')
r = insert(r, 'C')
r = insert(r, 'D')
r = insert(r, 'E')
r = insert(r, 'F')
r = insert(r, 'G')
r = insert(r, 'H')
r = insert(r, 'I')
r = insert(r, 'J')
r = insert(r, 'K')
r = insert(r, 'L')
r = insert(r, 'M')
r = insert(r, 'N')
r = insert(r, 'O')

ordered_insert(r)