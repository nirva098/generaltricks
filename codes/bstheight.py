'''
finding heiht of a bst recursively

height of tree = height of root node =
= max(height of left sub tree, height of right subtree) + 1

'''

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

    def height(self):
        if not self:
            return 0
        if (not self.left) and (not self.right):
            return 1
        hl, hr = 0,0
        if self.left:
            hl = self.left.height()
        if self.right:
            hr = self.right.height()
        return max(hl,hr)+1    

class Bst:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root:
            self.root.insert(val);
        else:
            self.root = Node(val)

    def height(self):
        if not self.root:
            return 0
        else:
            return self.root.height()



if __name__ == "__main__":
    '''
        10
       /  \
      5    15 
       \   /  \
        8 12  17

    height of this bst is 3
    '''
    b = Bst()
    b.insert(10)
    b.insert(5)
    b.insert(15)
    b.insert(8)
    b.insert(12)
    b.insert(17)

    print("Height of this bst is: ",b.height())
    
