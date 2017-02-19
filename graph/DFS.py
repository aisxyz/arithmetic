# coding: utf8

WHITE = 0     # before
GRAY = 1      # processing
BLACK = 2     # end

class Vertex:
    def __init__(self, key=None):
        self.key = key
        self.color = WHITE
        self.parent = None
        self.adjacent_vertexes = []
        self.start_visit_time = 0
        self.end_visit_time = 1

    def __repr__(self):
        return 'Vertex<key=%s, stime=%s, etime=%s>' % (
            self.key, self.start_visit_time, self.end_visit_time)


def DFS_visit(vertex, time):
    vertex.color = GRAY
    vertex.start_visit_time = time = time + 1
    for adj_vertex in vertex.adjacent_vertexes:
        if adj_vertex.color == WHITE:
            adj_vertex.parent = vertex
            time = DFS_visit(adj_vertex, time)
    vertex.color = BLACK
    vertex.end_visit_time = time = time + 1
    return time

def depth_first_search(graph):
    time = 0
    for vertex in graph:
        if vertex.color == WHITE:
            time = DFS_visit(vertex, time)


'''
def topo_logical_sort(G):
    call DFS(G) to computl finishing times f[v] for each vertex v
    as each vertex is finished, insert it onto the front of a linked list
    return the linked list of vertices
'''

'''
def strongly_connected_components(G):
    call DFS(G) to compute finishing times f[u] for each vertex u
    compute transpose(G) G_T
    call DFS(G_T), but in the main loop of DFS, consider the vertices in order
        of descreasing f[u]
    output the vertices of each tree in the depth-first forest formed in line 3
        as a seperate strongly connected component
'''

def vertex_walk(graph):
    for vertex in graph:
        print(vertex)

        
if __name__ == '__main__':
    vv = Vertex('v')
    vw = Vertex('w')
    vz = Vertex('z')
    vu = Vertex('u')
    vy = Vertex('y')
    vx = Vertex('x')

    vv.adjacent_vertexes = [vy]
    vw.adjacent_vertexes = [vy, vz]
    vz.adjacent_vertexes = [vz]
    vu.adjacent_vertexes = [vv, vx]
    vy.adjacent_vertexes = [vx]
    vx.adjacent_vertexes = [vv]

    graph = [vu, vv, vy, vx, vw, vz]
    vertex_walk(graph)
    print('='*50)
    depth_first_search(graph)
    vertex_walk(graph)
