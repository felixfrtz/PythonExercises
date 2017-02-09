from graph import *

def createGraphPath(n):
    """
    Creates a graph with n vertices and a edges, such
    that the path length is n-1
    :param n: number of vertices
    :return: The Graph
    """
    G = Graph(False)
    for i in range(0, n):
        G.add_vertex(Vertex(G))
    for j in range(0, len(G.vertices)-1):
        v1 = G.vertices[j]
        v2 = G.vertices[j+1]
        G+=Edge(v1,v2)
    return G

def createGraphCycle(n):
    G = Graph(False)
    for i in range(0, n):
        G.add_vertex(Vertex(G))
    for j in range(0, (len(G.vertices))):
        v1 = G.vertices[j]
        if j == ((len(G.vertices))-2):
            vlast = G.vertices[j+1]
            G += Edge(v1,vlast)
            G += Edge(vlast,G.vertices[0]);
            break
        else:
            v2 = G.vertices[j + 1]
            G += Edge(v1, v2)
    return G

# print(createGraphCycle(6))

a = createGraphPath(2)
b = createGraphCycle(3)
