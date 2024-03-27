import sys

from node import Node 
from bfs import BFS

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
        if counter == words:
            for word in wordLib:
                nodeList.append(Node(word, wordLib))
    else:
        ##queriesLib[splittedLine[0]] = splittedLine[1]
        BFS.algorithm(Node(splittedLine[0], wordLib), Node(splittedLine[1], wordLib), nodeList, wordLib)



