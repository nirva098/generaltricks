# level order traversal

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

    # bfs: breadth first search  and level order traversal is same way of traversing      
    def bfs(self):
        if not self:
            return
        q = []
        q.append(self)
        while len(q)>0:
            node = q.pop(0)
            print(node.value, end=" ")
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

            
    

class Bst:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root:
            self.root.insert(val);
        else:
            self.root = Node(val)
    def bfs(self):
        if self.root:
            self.root.bfs()
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
    level order traversal: 10 5 15 8 12 17
    '''
    b = Bst()
    b.insert(10)
    b.insert(5)
    b.insert(15)
    b.insert(8)
    b.insert(12)
    b.insert(17)

    b.bfs()
    
