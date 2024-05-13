import sys
from ff import Ff
from nodes import Nodes
from bfs import BFS

counter = 0
students = 0
edges = 0
nodes = 0
quiries = 0
dic = {}
matcher = {}
reNodes = []
for line in sys.stdin:
    lines = line.split()
    if counter == 0:
        nodes = lines[0]
        edges = lines[1]
        students = lines[2]
        quiries = lines[3]

        counter += 1
    elif counter < int(edges) + 1:

        ## !!! wichtich !!!! 
        ## måste poppa ett högre ur dic/matcher
        ## qiury  0 = dic.pop(matcher.pop(1)) ++ dic.pop(matcher.pop(-1))

        dic[lines[1], lines[0]] = lines[2]
        dic[lines[0], lines[1]] = lines[2]
        matcher[counter] = (lines[0], lines[1])
        matcher[-counter] = (lines[1], lines[0])
        counter += 1
    else:
        reNodes.append(line[0])
nodeList = {}
nodeList[0] = Nodes(0)
nodeList[1] = Nodes(1)
nodeList[2] = Nodes(2)
nodeList[3] = Nodes(3)

start = nodeList[0]
n1 = nodeList[1]
n2 = nodeList[2]
end = nodeList[3]
start.neighbour.append(n1)
n1.neighbour.append(end)
n1.neighbour.append(n2)
n2.neighbour.append(end)

print(BFS.bfs(start,end, nodeList))

counter = 0
# while reNodes:
#     flow = Ff.ff()
#     if flow >= students:
#         reNodes.remove[counter]
#         counter += 1
#     else:
#         reNodes = []

