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
def rb_fix_bblack(root, bbnode):
    if bbnode is None:
        return root

    print "bbnode: %d, color: %s" % (bbnode.getValue(), bbnode.color.name)
    parent = bbnode.getParent()

    #remove leaf means that delete a path
    if bbnode.color == Color.none_bblack:
        if parent.getLeft() == bbnode:
            parent.setLeft(None)
            if parent.getRight() is None:
                parent.setColor(Color.bblack)
        else:
            parent.setRight(None)
            if parent.getLeft() is None:
                parent.setColor(Color.bblack)
        bbnode = parent

#    print "color name: %s" % bbnode.color.name
#    print "val: %d" % bbnode.getValue()
    node = None
    brother = None
    while bbnode.color == Color.bblack:
        parent = bbnode.getParent()
        if parent is None:
            break

        if parent.getLeft() == bbnode:
            brother = parent.getRight()
            if brother and brother.color == Color.black:
                if brother.getLeft() and brother.getLeft().color == Color.red:
                    node = brother
                    root = rightRotation(root, brother)
                elif brother.getRight() and brother.getRight().color == Color.red:
                    node = brother.getRight()
                elif brother.getLeft() and brother.getRight() and \
                     brother.getLeft().color == Color.black and \
                     brother.getRight().color == Color.black:
                    set_color([bbnode, brother],[Color.black, Color.red])
                    rb_mkblk(parent)
                    bbnode = parent
                    continue

                set_color([parent, node],[Color.black, Color.black])
                root = leftRotation(root, parent)
#                rb_mkblk(bbnode)
            elif brother and brother.color == Color.red:    #brother is red
                set_color([parent, brother],[Color.red, Color.black])
                root = leftRotation(root, parent)
            rb_mkblk(bbnode)
        else:
            brother = parent.getLeft()
            if brother and brother.color == Color.black:
                if brother.getRight() and brother.getRight().color == Color.red:
                    node = brother
                    root = leftRotation(root, brother)
                elif brother.getLeft() and brother.getLeft().color == Color.red:
                    node = brother.getLeft()
                elif brother.getLeft() and brother.getRight() and \
                     brother.getLeft().color == Color.black and \
                     brother.getRight().color == Color.black:
                    set_color([bbnode, brother],[Color.black, Color.red])
                    rb_mkblk(parent)
                    bbnode = parent
                    continue

                set_color([parent, node],[Color.black, Color.black])
                root = rightRotation(root, parent)
#                rb_mkblk(bbnode)
            elif brother and brother.color == Color.red:    #brother is red
                set_color([parent, brother],[Color.red, Color.black])
                root = rightRotation(root, parent)
            rb_mkblk(bbnode)

    root.color = Color.black
    return root

def rb_delete(rbt_root, dnode):
    root = rbt_root
    x1 = dnode
    parent = None
    rmin = None

    if dnode is None or root is None:
        return root

    if root.getLeft() is None and root.getRight() is None:
        if root.getValue() == dnode.getValue():
            return None
        else:
            print "delete no-exist node."
            raise

    parent = dnode.getParent()

    if dnode.getLeft() is None and dnode.getRight() is None:
        dnode.setColor(Color.none_bblack)
    elif dnode.getLeft() is None:
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

        root = rb_fix_bblack(root, dnode)
        return root

    rb_mkblk(dnode)
    if parent is None:
        root = dnode
        dnode.setParent(None)
        root.setColor(Color.black)
    else:
        if parent.getLeft() == x1:
            parent.setLeft(dnode)
        else:
            parent.setRight(dnode)

#    x1.setParent(None)
    root = rb_fix_bblack(root, dnode)
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

#values = [3, 2, 1]
values = [1,2,3,4,5,6]
#values = [2,4,3,5,6]
def testRbt(vals):
#    rbt = TestRbt(vals)
#    rbt.rbtMiddleTraverse()
    rr = TestRbt(values)
#    rr.rbtMiddleTraverse()
    node = findNode(rr.root, 4)
#    rr.root = rightRotation(rr.root, node)
#    rr.root = leftRotation(rr.root, node)
    rr.root = rb_delete(rr.root, node)
#    br = node.getBrother()
#    print br.getValue()
    rr.rbtFirstTraverse()








































