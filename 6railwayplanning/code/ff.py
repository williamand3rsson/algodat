class Ff:
    def ff(students, nodes, edges):
        for e in edges:
            e.flow = 0
        totFlow = 0
        while totFlow <= students:
            snabbväg = bfs(nodes)
            totFlow += flowFf(snabbväg, edges)
        return totFlow