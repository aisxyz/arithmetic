# coding: utf8
from collections import deque

WHITE = 0     # before
GRAY = 1      # processing
BLACK = 2     # end

class Vertex:
    def __init__(self, key=None):
        self.key = key
        self.color = WHITE
        self.parent = None
        self.adjacent_vertexes = []
        self.distance_to_start_vertex = -1

    def __repr__(self):
        return 'Vertex<key=%s, d=%s>' % (
            self.key, self.distance_to_start_vertex)


def breadth_first_search(start_vertex):
    start_vertex.color = GRAY
    start_vertex.distance_to_start_vertex = 0
    gray_queue = deque()
    gray_queue.append(start_vertex)

    while gray_queue:
        current_vertex = gray_queue.popleft()
        for vertex in current_vertex.adjacent_vertexes:
            if vertex.color == WHITE:
                vertex.color = GRAY
                vertex.parent = current_vertex
                vertex.distance_to_start_vertex = current_vertex.distance_to_start_vertex + 1
                gray_queue.append(vertex)
        current_vertex.color = BLACK


def print_BFS_path(start_vertex, target_vertex):
    if target_vertex == start_vertex:
        print(start_vertex)
    elif target_vertex.parent:
        print_BFS_path(start_vertex, target_vertex.parent)
        print(target_vertex)
    else:
        print("no path from", start_vertex, "to", target_vertex, "exists!")

        
def vertex_walk(graph):
    for vertex in graph:
        print(vertex)

        
if __name__ == '__main__':
    vr = Vertex('r')
    vs = Vertex('s')
    vv = Vertex('v')
    vw = Vertex('w')
    vt = Vertex('t')
    vu = Vertex('u')
    vy = Vertex('y')
    vx = Vertex('x')

    vr.adjacent_vertexes = [vv, vs]
    vv.adjacent_vertexes = [vr]
    vs.adjacent_vertexes = [vr, vw]
    vw.adjacent_vertexes = [vs, vx, vt]
    vt.adjacent_vertexes = [vw, vu, vx]
    vu.adjacent_vertexes = [vt, vy, vx]
    vy.adjacent_vertexes = [vx, vu]
    vx.adjacent_vertexes = [vw, vy, vt, vu]

    graph = [vr, vs, vv, vw, vt, vu, vy, vx]
    vertex_walk(graph)
    print('='*50)
    breadth_first_search(vs)
    vertex_walk(graph)
    print('='*50)
    print_BFS_path(vs, vy)
