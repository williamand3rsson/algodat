class Ff:
    def ff(students, nodes, edges):
        for e in edges:
            e.flow = 0
        totFlow = 0
        while totFlow < students:
            path = bfs(start, end, nodeList)
            min = 0
            for node in path:
                min = 1
            #snabbväg = bfs(nodes)
            #totFlow += flowFf(snabbväg, edges)
        return totFlow
