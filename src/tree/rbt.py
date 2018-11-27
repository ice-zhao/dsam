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

def rb_mkblk(node):
    if node is not None:
        if node.getColor() == Color.red:
            node.setColor(Color.black)
        elif node.getColor() == Color.black:
            node.setColor(Color.bblack)
        elif node.getColor() == Color.bblack:
            node.setColor(Color.black)

    return node

#1. delete a black leaf.
# if the leaf has a brother, just delete it from parent. otherwise, set the
# parent as double black color.
def rb_fix_bblack(root, bbnode, bbparent):
    while(bbnode is None or (bbnode.color == Color.black)) and bbnode != root:
        if bbparent.getLeft() == bbnode:
            other = bbparent.getRight()
            if other.color == Color.red:
                set_color([bbparent,other],[Color.red,Color.black])
                root = leftRotation(root, bbparent)
                other = bbparent.getRight()
            if (other.getLeft() is None or other.getLeft().color == Color.black)\
            and (other.getRight() is None or other.getRight().color == Color.black):
                set_color([other],[Color.red])
                bbnode = bbparent
                bbparent = bbnode.getParent()
            else:
                if other.getRight() is None or other.getRight().color == Color.black:
                    set_color([other,other.getLeft()],[Color.red,Color.black])
                    root = rightRotation(root, other)
                    other = bbparent.getRight()
                set_color([other,bbparent,other.getRight()],\
                          [bbparent.color, Color.black, Color.black])
                root = leftRotation(root, bbparent)
                bbnode = root
                break
        else:
            other = bbparent.getLeft()
            if other.color == Color.red:
                set_color([bbparent,other],[Color.red,Color.black])
                root = rightRotation(root, bbparent)
                other = bbparent.getLeft()
            if (other.getLeft() is None or other.getLeft().color == Color.black)\
            and (other.getRight() is None or other.getRight().color == Color.black):
                set_color([other],[Color.red])
                bbnode = bbparent
                bbparent = bbnode.getParent()
            else:
                if other.getLeft() is None or other.getLeft().color == Color.black:
                    set_color([other,other.getRight()],[Color.red,Color.black])
                    root = leftRotation(root, other)
                    other = bbparent.getLeft()
                set_color([other, bbparent, other.getLeft()],\
                          [bbparent.color, Color.black, Color.black])
                root = rightRotation(root, bbparent)
                bbnode = root
                break
    if bbnode:
        bbnode.color = Color.black
    return root

def rb_delete(rbt_root, dnode):
    root = rbt_root
    parent = None
    child = None
    color = Color.noColor

    if dnode is None or root is None:
        return root

    if dnode.getLeft() is None:
        child = dnode.getRight()
    elif dnode.getRight() is None:
        child = dnode.getLeft()
    else:
        old = dnode
        dnode = minValue(dnode.getRight())

        color = dnode.getColor()
        child = dnode.getRight()
        parent = dnode.getParent()

        if parent == old:
            parent = dnode
        else:
            parent.setLeft(child)
            dnode.setRight(old.getRight())

        dnode.color = old.color
        dnode.setLeft(old.getLeft())

        if old.getParent():
            if old.getParent().getLeft() == old:
                old.getParent().setLeft(dnode)
            else:
                old.getParent().setRight(dnode)
        else:
            root = dnode
            root.setParent(None)

        if color == Color.black:
            root = rb_fix_bblack(root, child, parent)
        return root

    parent = dnode.getParent()
    color = dnode.getColor()

    if parent is None:
        root = child
        if root:
            root.setParent(None)
    else:
        if parent.getLeft() == dnode:
            parent.setLeft(child)
        else:
            parent.setRight(child)

    if color == Color.black:
        root = rb_fix_bblack(root, child, parent)
    return root


class TestRbt(object):
    def __init__(self, vals):
        self.node = None
        self.root = None
        self.dvalues = []
        for item in vals:
            self.node = rb_insert(self.node, item)
            self.dvalues.append(item)
        self.root = self.node

    def rbtMiddleTraverse(self):
        middleTraverse(self.root)

    def rbtFirstTraverse(self):
        FirstTraverse(self.root)

    def testDeleteNode(self):
        self.dvalues = [1,12,7,15,18,9,20,8]
        for i in self.dvalues:
            node = findNode(self.root, i)
            self.root = rb_delete(self.root, node)
        self.rbtFirstTraverse()
        if self.root is None:
            print "Empty red-black Tree"

values = [1,12,7,15,18,9,20,8,13]
def testRbt(vals):
    rr = TestRbt(values)
    rr.rbtFirstTraverse()
#    rr.testDeleteNode()








































