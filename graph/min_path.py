# coding: utf8

INFINITY = 9999

class Vertex:
    def __init__(self, key):
        self.key = key
        self.min_path = INFINITY
        self.parent = None
        self.adj_vertexes = []
        # self.out_degree = []
        # self.in_degree = []

    def __repr__(self):
        return "<Vertex(key=%s, min_path=%d)>" %(self.key, self.min_path)


def relax(vertex1, vertex2, weight):    # 松弛技术
    if vertex2.min_path > vertex1.min_path + weight:
        vertex2.min_path = vertex1.min_path + weight
        vertex2.parent = vertex1

def check_circle_path_with_negative_weight(graph, edges, sourceV):  # Bellman-Ford version
    sourceV.min_path = 0
    for _ in range(1, len(graph)):
        for weight, v1, v2 in edges:
            relax(v1, v2, weight)
            
    for weight, v1, v2 in edges:
        if v2.min_path > v1.min_path + weight:
            return False
    return True


def extract_min_path_vertex(graph):
    vertex = graph[0]
    for v in graph[1:]:
        if vertex.min_path > v.min_path:
            vertex = v
    graph.remove(vertex)
    return vertex

def compute_min_path(graph, sourceV):   # Dijkstra version
    """All weights must be above 0."""
    sourceV.min_path = 0
    temp_graph = [v for v in graph]
    while temp_graph:
        v1 = extract_min_path_vertex(temp_graph)
        for w, adjV in v1.adj_vertexes:
            relax(v1, adjV, w)
            
        
if __name__ == "__main__":
    vs = Vertex('s')
    vt = Vertex('t')
    vx = Vertex('x')
    vy = Vertex('y')
    vz = Vertex('z')

    graph = [vs, vt, vx, vy, vz]
    '''
    edges = [(6, vs, vt), (7, vs, vy), (5, vt, vx), (8, vt, vy), (-4, vt, vz),
             (-2, vx, vt), (-3, vy, vx), (9, vy, vz), (2, vz, vs), (7, vz, vx)]

    print(check_circle_path_with_negative_weight(graph, edges, vs))
    '''
    vs.adj_vertexes = [(10, vt), (5, vy)]
    vt.adj_vertexes = [(1, vx), (2, vy)]
    vx.adj_vertexes = [(4, vz)]
    vy.adj_vertexes = [(3, vt), (2, vz), (9, vx)]
    vz.adj_vertexes = [(6, vx), (7, vs)]

    compute_min_path(graph, vs)

    for v in graph:
        print(v, '<--', v.parent)
