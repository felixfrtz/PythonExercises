from graph import *
from graph_io import *
from exc1 import *

def bfs(s: Vertex):
    queue = [s]
    visited = list()
    visitcounter = 0
    while len(queue) > 0:
        print(queue)
        v = queue[0]
        v.label = visitcounter
        v.colortext = 'Blue'
        v.colornum = 1

        visitcounter += 1

        if v not in visited:
            visited.append(v)
        queue.remove(v)

        for i in v.neighbours:
            if i not in visited:
                queue.append(i)

    return visited


with open('examplegraph.gr') as e:
    a = load_graph(e)

with open('original.gr', 'w') as c:
    write_dot(a, c)

print(bfs(a.vertices[0]))

with open('visitedgraph.dot', 'w') as f:
    write_dot(a, f)

