import sys
import math
from node import Node
from jarnik import Jarnik
#weightedGraph = []
counter = 0

# for line in sys.stdin:
#     nbrs = line.split()
#     if counter == 0:
#         lista = [num for num in range(1, int(nbrs[0]) + 1)]
#         rows = int(nbrs[0])
#         cols = int(nbrs[1])
#         graf = []
#         graf = [[0] * rows for _ in range(rows)]
#         counter += 1
#     else : 
#         graf[int(nbrs[1])-1][int(nbrs[0])-1] = int(nbrs[2])
#         graf[int(nbrs[0])-1][int(nbrs[1])-1] = int(nbrs[2])

for line in sys.stdin:
    nbrs = line.split()
    if counter == 0:
        nodeDic = {}
        for n in range(int(nbrs[0])):
            node = Node(n)  
            nodeDic[n] = node 
        counter += 1
    else : 
        nodeDic[int(nbrs[0])].addEdge(int(nbrs[2]), int(nbrs[1]))
        
graph = {}
for key, value in nodeDic.items():
    graph[value] = value.edges
Jarnik.jarnik(graph, nodeDic.pop(1), nodeDic)
#print(graph)
#print(graf)
#print(node)
    

            