from queue import PriorityQueue

class Jarnik:

    def jarnik(graf, root, nodeDic):
        T = 0
        Q = nodeDic
        currentNode = root
        consider = PriorityQueue()
        while (len(Q) != 0):
            #Notfound = True
            # for v in consider:
            #     if(v in Q):
            #         rv = v
            #         NotFound = False
            for v in currentNode.edges:
                if v[0] in Q:
                    consider.put(v[1], (v[0], v[1]))
            Q.pop(v[0])
            T += + v[1]
            currentNode = nodeDic[v[0]]
        return T