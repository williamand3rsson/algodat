import math

class Node:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distanceTo(self, other):
        return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
