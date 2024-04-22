from queue import PriorityQueue

class Jarnik:

    def jarnik(graf, root, nodeDic):
        T = None
        nodeDic.pop(root) 
        Q = nodeDic
        currentNode = root
        consider = PriorityQueue()
        while (len(Q) != 0):
            Notfound = true
            while NotFound:
                tuplar = currentNode.edges.get()
                if(tuplar[0] in Q):
                    NotFound = false
            for (nb, prio) in currentNode.edges:
                consider.put(prio, (nb, prio))
            Q.pop(v)
            T = T + tuplar[1]
            currentNode = v
