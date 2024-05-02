import sys
from node import Node
from util import Util

counter = 0
nbrElem = None
points = []
for line in sys.stdin:
    if counter == 0:
        nbrElem = int(line) + 1
        counter += 1
    else : 
        nbrs = line.split()
        points.append(Node(int(nbrs[0]), int(nbrs[1])))
        counter += 1

Px = points[:]
Py = points[:]
Px = sorted(points, key=lambda node: node.x)
Py = sorted(points, key=lambda node: node.y)
util = Util()
print(format(Util.closest(Px, Py, len(Px)), ".6f"))
