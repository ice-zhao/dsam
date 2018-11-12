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
    xnode = ynode.getLeft()
    yright = ynode.getRight()

    if xnode is None:
        return rbt

    xleft = xnode.getLeft()
    xright = xnode.getRight()

    replace(ynode, xnode)
    setChildren(ynode, xright, yright)
    setChildren(xnode, xleft, ynode)

    if parent is None:
        return rbt

















































