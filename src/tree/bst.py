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
        print bst.getValue()
        FirstTraverse(bst.getLeft())
        FirstTraverse(bst.getRight())

    return


def middleTraverse(bst):
    if bst is not None:
        middleTraverse(bst.getLeft())
        print bst.getValue()
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










def testBst(vals):
    node = None
    for item in vals:
        node = insertNode(node, item)

    bst = node

#    FirstTraverse(bst)
#    middleTraverse(bst)
#    lastTraverse(bst)

    node = findNode(bst, 6)
    succ = successorBst(node)
    pred = predecessorBst(node)
    try:
        val= succ.getValue()
        pred_val = pred.getValue()
    except Exception, e:
        print e
    else:
#        print val
#        print pred_val
        pass

#    tree = deleteNode(bst, node)
#    node = findNode(bst, 7)
#    tree = deleteNode(bst, node)
##    middleTraverse(tree)
#
#    node = findNode(bst, 9)
#    print node.getParent().getValue()
    return node















