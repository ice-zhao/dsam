#red-black Tree

from common import *
from bst import *

def replace(xnode, ynode):
    if xnode is None:
        return

    parent = xnode.getParent()

    if parent is None:
        if ynode is not None:
            ynode.setParent(parent)
    elif parent.getLeft() == xnode:
        parent.setLeft(ynode)
    else:
        parent.setRight(ynode)

    xnode.setParent(None)


def setChildren(node, lnode, rnode):
    if node is not None:
        node.setLeft(lnode)
        node.setRight(rnode)


def leftRotation(rbt, xnode):
    if rbt is None or xnode is None:
        return rbt

    parent = xnode.getParent()
    xright = xnode.getRight()
    xleft = xnode.getLeft()

    if xright is None:
        return rbt

    xr_left = xright.getLeft()
    xr_right = xright.getRight()

    replace(xnode, xright)
    setChildren(xnode, xleft, xr_left)
    setChildren(xright, xnode, xr_right)

    if parent is None:
        rbt = xright
    else:
        parent.setRight(xright)

    return rbt


def rightRotation(rbt, ynode):
    if rbt is None or ynode is None:
        return rbt

    parent = ynode.getParent()
    yleft = ynode.getLeft()
    yright = ynode.getRight()

    if yleft is None:
        return rbt

    yl_left = yleft.getLeft()
    yl_right = yleft.getRight()

    replace(ynode, yleft)
    setChildren(ynode, yl_right, yright)
    setChildren(yleft, yl_left, ynode)

    if parent is None:
        rbt = yleft
    else:
        parent.setLeft(yleft)

    return rbt

def set_color(nodes, colors):
    if len(nodes) == 0 or len(colors) == 0:
        print "set_color size is 0."
        raise
    if len(nodes) == len(colors):
        for i in range(len(nodes)):
            nodes[i].color = colors[i]
    return

def rb_insert_fix(root, node):
    while( node.getParent() and node.getParent().color == Color.red ):
        parent = node.getParent()
        uncle = node.getUncle()
        grandparent = node.getGrandparent()

        if uncle and uncle.color == Color.red:
            set_color([parent,    grandparent, uncle], \
                      [Color.black, Color.red, Color.black])
            node = node.getGrandparent()
        else:
            if grandparent and grandparent.getLeft() == parent:
                if parent.getRight() == node:  #left-right type, two times rotation
                    node = parent
                    root = leftRotation(root, node)
                    parent = node.getParent()
                    grandparent = node.getGrandparent()
                set_color([parent, grandparent], [Color.black, Color.red])
                root = rightRotation(root, grandparent)
            elif grandparent and grandparent.getRight() == parent:
                if parent.getLeft() == node:        #right-left type
                    node = parent
                    root = rightRotation(root, node)
                    parent = node.getParent()
                    grandparent = node.getGrandparent()
                set_color([parent, grandparent], [Color.black, Color.red])
                root = leftRotation(root, grandparent)
    root.color = Color.black
    return root


def rb_insert(rbt, val):
    root = rbt
    node = Node(val)
    parent = None

    while rbt is not None:
        parent = rbt
        if rbt.getValue() == val:
            print "Red-black tree has this %d value." % val
            break
#            return root

        if val < rbt.getValue():
            rbt = rbt.getLeft()
        else:
            rbt = rbt.getRight()

    if parent is None:
        root = node
    elif val < parent.getValue():
        parent.setLeft(node)
    else:
        parent.setRight(node)

    root = rb_insert_fix(root, node)
    return root


class TestRbt(object):
    def __init__(self, vals):
        self.node = None
        self.root = None
        for item in vals:
            self.node = rb_insert(self.node, item)
        self.root = self.node

    def rbtMiddleTraverse(self):
        middleTraverse(self.root)

    def rbtFirstTraverse(self):
        FirstTraverse(self.root)

values = [3, 2, 1]
#values = [1,2,3,4,5,6,7,8]
def testRbt(vals):
#    rbt = TestRbt(vals)
#    rbt.rbtMiddleTraverse()
    rr = TestRbt(values)
#    rr.rbtMiddleTraverse()
#    node = findNode(rr.root, 1)
#    rr.root = rightRotation(rr.root, node)
#    rr.root = leftRotation(rr.root, node)
    rr.rbtFirstTraverse()








































