from enum import Enum

class Color(Enum):
    RED = 1
    BLACK = 2

class Node:
    def __init__(self, color, key, left, right, parent):
        self.color = color
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent
