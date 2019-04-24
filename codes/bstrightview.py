# binary search tree
# printing left view and right view of a binary tree
# interative inorder is reference for printleftview
# iterative reverseInorder is reference for printrightview

class Node:
    level = 1
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        self.level = 1
        
    def insert(self, data):
        # no dups allowed
        if self.value == data:
            return False
        elif data<self.value:
            if self.left:
                Node.level += 1
                return self.left.insert(data)
            else:
                Node.level += 1
                self.left = Node(data)
                self.left.level = Node.level
                Node.level = 1
                return True
        else:
            if self.right:
                Node.level += 1
                return self.right.insert(data)
            else:
                Node.level += 1
                self.right = Node(data)
                self.right.level = Node.level
                Node.level = 1
                return True
            
    def height(self):
        if not self:
            return 0
        if (not self.left) and (not self.right):
            return 1
        hl,hr = 0,0
        if self.left:
            hl = self.left.height()
        if self.right:
            hr = self.right.height()
        return max(hr,hl)+1
        
    
        

class Bst:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root:
            self.root.insert(val);
        else:
            self.root = Node(val)
    def height(self):
        if self.root:
            return self.root.height()
        else:
            print("Tree is empty")

    def inorder(self):
        root = self.root
        s = []
        while True:
            if root:
                s.append(root)
                root = root.left
            else:
                if not s:
                    break
                else:
                    root = s.pop()
                    print(root.value, end=" ")
                    root = root.right
                    
    def printleftview(self):
        h = self.height()
        root = self.root
        s = []
        lv = [False for i in range(h)]
        while True:
            if root:
                s.append(root)
                root = root.left
            else:
                if not s:
                    break
                else:
                    root = s.pop()
                    val = root.value
                    if not lv[root.level-1]:
                        lv[root.level-1] = val
                    root = root.right
        print(lv)

    def reverseInorder(self):
        s = []
        root = self.root
        while True:
            if root:
                s.append(root)
                root = root.right
            else:
                if not s:
                    break
                else:
                    root = s.pop()
                    print(root.value, end=" ")
                    root = root.left

    def printrightview(self):
        h = self.height()
        rv = [False for i in range(h)]
        s = []
        root = self.root

        while True:
            if root:
                s.append(root)
                root = root.right
            else:
                if not s:
                    break
                else:
                    root = s.pop()
                    lvl = root.level
                    val = root.value
                    if not rv[lvl-1]:
                        rv[lvl-1] = val
                    root = root.left
        print(rv)
    
        

    

if __name__ == "__main__":
    '''
        10
       /  \
      5    15 
       \   /  \
        8 12  17
       /   \
      6     13

    height of this bst is 3
    '''
    b = Bst()
    b.insert(10)
    b.insert(5)
    b.insert(15)
    b.insert(8)
    b.insert(6)
    b.insert(12)
    b.insert(13)
    b.insert(17)
    print("Left view of this bst:")
    b.printleftview()
    print("Right view of this bst:")
    b.printrightview()
