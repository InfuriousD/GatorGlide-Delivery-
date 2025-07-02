class treeNode(object):
    def __init__(self, orderId, currentSystemTime, orderValue, deliveryTime, ETA, priority) -> None:
        self.id = orderId
        self.createTime = currentSystemTime
        self.value = orderValue
        self.deliveryTime = deliveryTime
        self.eta = ETA
        self.priority = priority

        #Treess
        self.leftChild = None
        self.rightChild = None
        self.parent = None
        self.height = 1
    
    def updateHeight(self):
        leftHeight = 0 if not self.leftChild else self.leftChild.height
        rightheight = 0 if not self.rightChild else self.rightChild.height
        self.height = max(leftHeight, rightheight) + 1

class avlTree(object):
    def __init__(self) -> None:
        self.root = None
        
    def insert(self, cur, node):
        if not cur:
            self.root = node
            cur = self.root
        elif node.priority > cur.priority:
            if cur.rightChild:
                self.insert(cur.rightChild, node)
            else:
                cur.rightChild = node
                node.parent = cur
        else:
            if cur.leftChild:
                self.insert(cur.leftChild, node)
            else:
                cur.leftChild = node
                node.parent = cur
        
        cur.updateHeight()

        # Balancing the tree
        self.balanceTree(cur)

    def delete(self, cur, key, id):
        if not cur:
            
            return
        
        elif cur.id == id:
            parent = cur.parent
            # found key
            # order of node is less than two, simple
            if not cur.leftChild:
                # it either only has a right child or has none
                # cur = cur.rightChild
                if parent is None:
                    if cur.rightChild is None:
                        self.root = None
                    else:
                        self.root = cur.rightChild
                        cur.parent = None
                else:
                    if cur.rightChild is None:
                        if parent.leftChild == cur:
                            parent.leftChild = None
                        else:
                            parent.rightChild = None
                    else:
                        if parent.leftChild == cur:
                            parent.leftChild = cur.rightChild
                            cur.rightChild.parent = parent
                        else:
                            parent.rightChild = cur.rightChild
                            cur.rightChild.parent = parent
                cur = cur.rightChild

            elif not cur.rightChild:
                parent = cur.parent
                if not parent:
                    self.root = cur.leftChild
                    cur.leftChild.parent = None
                else:
                    if parent.leftChild == cur:
                        parent.leftChild = cur.leftChild
                        cur.leftChild.parent = parent
                    else:
                        parent.rightChild = cur.leftChild
                        cur.leftChild.parent = parent
                cur = cur.leftChild

            # order of node is two means that it has both the right and left children
            else:
                # finding min in right subtree, Swaping them and deleting.
                minNode = self.getMin(cur.rightChild)
                self.nodeSwap(cur, minNode)
                self.delete(cur, key, id)
        
        elif key > cur.priority:
            self.delete(cur.rightChild, key, id)
        elif key <= cur.priority:
            self.delete(cur.leftChild, key, id)
        
        if cur:
            # update height
            cur.updateHeight()

            # balance tree
            self.balanceTree(cur)

    def rRotate(self, x, y):
        parent = x.parent

        yl = y.leftChild
        y.leftChild = x
        x.parent = y
        x.rightChild = yl
        if yl:
            yl.parent = x
        y.parent = parent

        x.updateHeight()
        y.updateHeight()

        if not parent:
            self.root = y
        elif parent.leftChild == x:
            parent.leftChild = y
            parent.updateHeight()
        elif parent.rightChild == x:
            parent.rightChild = y
            parent.updateHeight()

    def lRotate(self, x, y):
        parent = x.parent

        tp = y.rightChild
        y.rightChild = x
        x.parent = y
        x.leftChild = tp
        if tp:
            tp.parent = x
        y.parent = parent

        x.updateHeight()
        y.updateHeight()

        if not parent:
            self.root = y
        elif parent.leftChild == x:
            parent.leftChild = y
            parent.updateHeight()
        elif parent.rightChild == x:
            parent.rightChild = y
            parent.updateHeight()

    def rlRotate(self, x, y, z):
        self.lRotate(y, z)
        self.rRotate(x, z)

    def lrRotate(self, x, y, z):
        self.rRotate(y, z)
        self.lRotate(x, z)
    
    def balanceTree(self, cur):
        if not cur:
            return
        if self.getBf(cur) < -1:
            if self.getBf(cur.rightChild) == 1:
                self.rlRotate(cur, cur.rightChild, cur.rightChild.leftChild)
            else:
                self.rRotate(cur, cur.rightChild)

        elif self.getBf(cur) > 1:
            if self.getBf(cur.leftChild) == -1:
                self.lrRotate(cur, cur.leftChild, cur.leftChild.rightChild)
            else:
                self.lRotate(cur, cur.leftChild)

    @staticmethod
    def getBf(node):
        if not node.leftChild and not node.rightChild:
            return 0
        elif not node.leftChild:
            return -node.rightChild.height
        elif not node.rightChild:
            return node.leftChild.height
        else:
            return node.leftChild.height - node.rightChild.height
        
    @staticmethod
    def getMin(node):
     #Check whether the leftnode is none or not.
     while node is not None and node.leftChild is not None:
        node = node.leftChild
     return node

    
    @staticmethod
    def nodeSwap(x, y):
        tmp = [x.id, x.createTime, x.value, x.deliveryTime, x.eta, x.priority]

        x.id = y.id
        x.createTime = y.createTime
        x.value = y.value
        x.deliveryTime = y.deliveryTime
        x.eta = y.eta
        x.priority = y.priority

        y.id = tmp[0]
        y.createTime = tmp[1]
        y.value = tmp[2]
        y.deliveryTime = tmp[3]
        y.eta = tmp[4]
        y.priority = tmp[5]
