from queue import PriorityQueue

class Jarnik:

    def jarnik(graf, root, nodeDic):
        T = 0
        Q = nodeDic.copy()
        Q.pop(1) 
        currentNode = root
        consider = PriorityQueue()
        while (len(Q) != 1):
            for v in currentNode.edges:  
                if v[0] in Q:
                    consider.put((v[1], (v[0], v[1])))
            b = True
            while b:
                priority, (target, prio2) = consider.get()
                if target in Q:
                    currentNode = nodeDic.get(target)
                    Q.pop(target)
                    T += priority
                    b = False
        return T