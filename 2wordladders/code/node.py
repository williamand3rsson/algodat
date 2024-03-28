class Node:

    def __init__(self, name, wordLib):
        self.name = name
        self.neighbourList = self.findNeighbour(wordLib)
        self.visited = 0
        self.pred = None
    
    def findNeighbour(self, wordLib):
        nbList = []
        for nb in wordLib:
            fourLetterWord = self.name[1:]
            temp = nb
            for c in fourLetterWord:
                nb = nb.replace(c, "", 1)
            if len(nb) == 1:
                nbList.append(temp)
        nbList.remove(self.name)
        return nbList
    
    def __str__(self):
        return f"{self.name}"