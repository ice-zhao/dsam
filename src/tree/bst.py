#binary search tree
from common import *



def insertNode(root, val):
    itoroot = root
    parent = None
    key=Node(val)

    while itoroot is not None:
        parent = itoroot

        if val < itoroot.getValue():
            itoroot = itoroot.getLeft()
        elif val > itoroot.getValue():
            itoroot = itoroot.getRight()

    if parent is None:    #tree is empty
        return key
    if val < parent.getValue():
        parent.setLeft(key)
    if val > parent.getValue():
        parent.setRight(key)

#    key.setParent(parent)

    return root


def FirstTraverse(bst):
    if bst is not None:
        print "%d,  %s" % (bst.getValue(), bst.color.name)
        FirstTraverse(bst.getLeft())
        FirstTraverse(bst.getRight())

    return


def middleTraverse(bst):
    if bst is not None:
        middleTraverse(bst.getLeft())
        print "%d,  %s" % (bst.getValue(), bst.color.name)
        middleTraverse(bst.getRight())

    return


def lastTraverse(bst):
    if bst is not None:
        lastTraverse(bst.getLeft())
        lastTraverse(bst.getRight())
        print bst.getValue()

    return

def findNode(bst, val):
    node = None
    itor_bst = bst
    while itor_bst is not None:
        if val == itor_bst.getValue():    #find it
            node = itor_bst
            break
        elif val < itor_bst.getValue():
            itor_bst = itor_bst.getLeft()
        elif val > itor_bst.getValue():
            itor_bst = itor_bst.getRight()

    return node

#find minimum value in BST
def minValue(bst):
    node = bst
    itor_bst = bst
    while itor_bst is not None:
        if itor_bst.getLeft() is not None:
            node = itor_bst.getLeft()
        itor_bst = itor_bst.getLeft()

    return node


#find maximum value in BST
def maxValue(bst):
    node = bst
    itor_bst = bst
    while itor_bst is not None:
        if itor_bst.getRight() is not None:
            node = itor_bst.getRight()
        itor_bst = itor_bst.getRight()

    return node


def successorBst(bst):
    itor_bst = bst
    parent = None
    right_node = itor_bst.getRight()

    if right_node is not None:
        return minValue(right_node)
    else:
        parent = itor_bst.getParent()
        while parent is not None and itor_bst == parent.getRight():
            itor_bst = parent
            parent = parent.getParent()

    return parent

def predecessorBst(bst):
    itor_bst = bst
    parent = None
    left_node = bst.getLeft()

    if left_node is not None:
        return maxValue(left_node)
    else:
        parent = bst.getParent()
        while parent is not None and parent.getLeft() == itor_bst:
            itor_bst = parent
            parent = parent.getParent()

    return parent


def deleteNode(bst, dnode):
    root = bst
    x1 = dnode
    parent = None
    rmin = None

    if dnode is None or root is None:
        return root

    parent = dnode.getParent()

    if dnode.getLeft() is None:
        dnode = dnode.getRight()
        x1.setRight(None)
    elif dnode.getRight() is None:
        dnode = dnode.getLeft()
        x1.setLeft(None)
    else:
        rmin = minValue(dnode.getRight())
        dnode.setValue(rmin.getValue())
        parent = rmin.getParent()
        rmin_right = rmin.getRight()

        if parent != dnode:
            parent.setLeft(rmin_right)
        else:
            parent.setRight(rmin_right)
        #delete rmin
        rmin.setParent(None)
        if rmin_right is not None:
            rmin.setRight(None)

        return root

    if parent is None:
        root = dnode
        dnode.setParent(None)
    else:
        if parent.getLeft() == x1:
            parent.setLeft(dnode)
        else:
            parent.setRight(dnode)

    x1.setParent(None)

    return root






class TestBst(object):
    def __init__(self, vals):
        self.node = None
        self.bst = None
        for item in vals:
            self.node = insertNode(self.node, item)
        self.bst = self.node

    def testSuccessorAndPredecessor(self):
        #test successor or predecessor of one node
        node = findNode(self.bst, 6)
        succ = successorBst(node)
        pred = predecessorBst(node)
        try:
            val= succ.getValue()
            pred_val = pred.getValue()
        except Exception, e:
            print e
        else:
            print val
            print pred_val

    def testDeleteNode(self):
        #test delete one node
        node = findNode(self.bst, 6)
        tree = deleteNode(self.bst, node)
        node = findNode(self.bst, 7)
        tree = deleteNode(self.bst, node)
    #    middleTraverse(tree)

        node = findNode(self.bst, 9)
        print node.getParent().getValue()

    def testGetParent(self):
        #test get grandparent
        nodex = findNode(self.bst, 2)
        if nodex is not None:
            grandparent = nodex.getGrandparent()
            if grandparent is not None:
                print "grandparent of %d: %d" % (nodex.getValue(), grandparent.getValue())
            else:
                print "can't find node %d's grandparent." % nodex.getValue()

    def testGetUncle(self):
        #test get uncle
        nodex = findNode(self.bst, 1)
        if nodex is not None:
            uncle = nodex.getUncle()
            if uncle is not None:
                print "uncle of %d: %d" % (nodex.getValue(), uncle.getValue())
            else:
                print "can't find node %d's uncle." % nodex.getValue()






def testBst(vals):
    mybst = TestBst(vals)
#    FirstTraverse(mybst.bst)
#    middleTraverse(mybst.bst)
#    lastTraverse(mybst.bst)
#    mybst.testGetUncle()
    return mybst















