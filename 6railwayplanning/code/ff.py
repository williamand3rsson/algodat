class Ff:
    def ff(students, edges, path, totFlow):
        mini = 696969
        for i in range(len(path)-1):
            newEdge = edges[(path[i], path[i+1])]
            mini = min(mini, newEdge.totC())
            if mini == 0:
                return totFlow
            
        for i in range(len(path)-1):
            frontEdge = edges[(path[i], path[i+1])]
            backEdge = edges[(path[i+1], path[i])]
            frontEdge.flow += mini
            backEdge.flow -= mini
        return totFlow + mini

        

        
            