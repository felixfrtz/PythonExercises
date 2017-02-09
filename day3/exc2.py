from graph_io import *
from graph import *
from exc1 import *

# with open('examplegraph.gr') as f:
#     G = load_graph(f)
# print(G)
# v, w, *remainder = G.vertices
# G.add_edge(Edge(v,w))
# with open('examplegraph2.gr', 'w') as f:
#     save_graph(G, f)


def complement(input):
    vertexmap = {}
    R = Graph(False)


    for i in G.vertices:
        vertexmap[i] = Vertex(R)
        R.add_vertex(vertexmap[i])

    for u in G.vertices:
        for v in G.vertices:
            if v != u:
                if len(G.find_edge(u, v)) == 0 and len(R.find_edge(vertexmap[v], vertexmap[u])) == 0 and \
                                len(R.find_edge(vertexmap[u], vertexmap[v])) == 0:
                    e = Edge(vertexmap[u], vertexmap[v])
                    R.add_edge(e)


    return R



H = createGraphCycle(4)
print(H)
with open('H.gr', 'w') as h:
    save_graph(H, h)
R = complement('H.gr')

with open('mygraph.dot', 'w') as h:
    write_dot(R, h)
with open('mygraph2.dot', 'w') as h2:
    write_dot(H, h2)