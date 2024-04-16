import sys
import math
#weightedGraph = []
counter = 0

for line in sys.stdin:
    nbrs = line.split()
    if counter == 0:
        lista = [num for num in range(1, int(nbrs[0]) + 1)]
        rows = int(nbrs[0])
        cols = int(nbrs[1])
        graf = []
        graf = [[0] * rows for _ in range(rows)]
        counter += 1
    else : 
        graf[int(nbrs[1])-1][int(nbrs[0])-1] = int(nbrs[2])
        graf[int(nbrs[0])-1][int(nbrs[1])-1] = int(nbrs[2])
print(graf)
print(lista)
    

            