from enum import Enum

class Color(Enum):
    red = 1
    black = 2
    bblack = 3    #double black used for delete one rb node.
    noColor = -1

class Node(object):
    def __init__(self, val=0):
        self.value = val
        self.parent = None
        self.left = None
        self.right = None
        self.color = Color.noColor

    def getLeft(self):
        return self.left

    def setLeft(self, node):
        self.left = node
        if node is not None:
            node.setParent(self)

    def getRight(self):
        return self.right

    def setRight(self, node):
        self.right = node
        if node is not None:
            node.setParent(self)

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def getColor(self):
        return self.color

    def setColor(self, newColor):
        oldColor = self.color
        self.color = newColor
        return oldColor














