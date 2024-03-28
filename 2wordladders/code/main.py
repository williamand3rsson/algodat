import sys

from node import Node 
from bfs import BFS

#Saker att fixa för att programmet inte ska ta 2 timmar att köra (förhoppningsvis):
#   skapa noder i grannlistan i nodklasser
#   enbart skapa grannoderna när de väl behövs
#   mäta tid algortim: behöver skapa queriesLib = [][]  
#   göra vistited till en boolean
#   lista ut vad pred ska användas till
#   chilla galet  

counter = 0
words = 0
queries = 0
wordLib = []
nodeList = []
queriesLib = {}

for line in sys.stdin:
    splittedLine = line.split()
    if counter == 0:
        words = int(splittedLine[0])
        queries = int(splittedLine[1])
        counter = 1
    elif counter <= (words):
        wordLib.append(splittedLine[0])
        counter += 1
        if counter == words + 1:
            for word in wordLib:
                nodeList.append(Node(word, wordLib))
    else:
        BFS.algorithm(Node(splittedLine[0], wordLib), Node(splittedLine[1], wordLib), nodeList, wordLib)



