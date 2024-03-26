import sys

from node import Node 

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
    else:
        queriesLib[splittedLine[0]] = splittedLine[1]

for word in wordLib:
    nodeList.append(Node(word, wordLib))
