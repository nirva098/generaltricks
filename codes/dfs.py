# dfs in bst
# preorder, inorder and post order

class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
    def insert(self, data):

        # no dups allowed
        if self.value == data:
            return False
        elif data<self.value:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True
    def preorder(self):
        if self.value:
            print(self.value, end= " ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.value, end= " ")
        if self.right:
            self.right.inorder()
            
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.value, end= " ")
    

class Bst:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root:
            self.root.insert(val);
        else:
            self.root = Node(val)

    def preorder(self):
        if self.root:
            self.root.preorder()
        else:
            print("Tree is empty!")
    def inorder(self):
        if self.root:
            self.root.inorder()
        else:
            print("Tree is empty!")
        
    def postorder(self):
        if self.root:
            self.root.postorder()
        else:
            print("Tree is empty!")


if __name__ == "__main__":
    print("Welcome!")
    '''
        10
       /  \
      5    15 
       \   /  \
        8 12  17

    making this tree
    preorder: 10 5 8 15 12 17
    inorder: 5 8 10 12 15 17
    postorder: 8 5 12 17 15 10
    '''
    b = Bst()
    b.insert(10)
    b.insert(5)
    b.insert(15)
    b.insert(8)
    b.insert(12)
    b.insert(17)

    print()
    b.preorder()
    print()
    b.inorder()
    print()
    b.postorder()
