class Node:

    def __init__(self, name, wordLib):
        self.name = name
        self.neighbourList = self.findNeighbour(wordLib)
    
    def findNeighbour(self, wordLib):
        nbList = []
        for nb in wordLib:
            fourLetterWord = self.name[1:]
            temp = nb
            for c in fourLetterWord:
                nb = nb.replace(c, "", 1)
            if len(nb) == 1:
                nbList.append(temp)
        #print(nbList)
        return nbList