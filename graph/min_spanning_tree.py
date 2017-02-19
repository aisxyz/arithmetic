# coding: utf8

class Vertex:
    def __init__(self, key=None):
        self.key = key
        self.adj_vertexes = []

    def __repr__(self):
        return '<Vertex(key=%s>' %(self.key)


def min_spanning_tree(edges):   # Kruskal version
    MST_edges = []
    vertexes = set()
    connected_graph_set = []
    for edge in sorted(edges, key=lambda e: e[0]):
        vpairs = edge[1]
        is_in_same_graph = False
        if vpairs[0] not in vertexes and vpairs[1] not in vertexes:
            connected_graph_set.append(list(vpairs))
        elif vpairs[0] in vertexes and vpairs[1] in vertexes:
            i = j = -1
            index = 0
            for connected_graph in connected_graph_set:
                if i==-1 and vpairs[0] in connected_graph:
                    i = index
                if j==-1 and vpairs[1] in connected_graph:
                    j = index
                index += 1
                if i!=-1 and i==j:
                    is_in_same_graph = True
                    break
            else:
                connected_graph_set[i].extend(connected_graph_set[j])
                connected_graph_set.remove(connected_graph_set[j])
        else:
            for connected_graph in connected_graph_set:
                if vpairs[0] in connected_graph:
                    connected_graph.append(vpairs[1])
                    break
                if vpairs[1] in connected_graph:
                    connected_graph.append(vpairs[0])
                    break
        if is_in_same_graph:
            continue
        MST_edges.append(edge)
        vertexes.update(vpairs)
    return MST_edges


def MST(ngraph):   # Prim version
    infinity = 99999
    graph = [v for v in ngraph]
    graph.sort(key=lambda x: x.key, reverse=True)
    for v in graph:
        v.min_d_to_tree = infinity
        v.parent = None
    #startV = graph[-1]       # We suppose the tail vertex as the root of MST.
    #startV.min_d_to_tree = 0
    while graph:
        vertex = graph.pop()
        for w, adjV in vertex.adj_vertexes:
            if adjV in graph and w < adjV.min_d_to_tree:
                adjV.min_d_to_tree = w
                adjV.parent = vertex

def walk_MST(graph):
    for v in graph:
        print(v, '<--', v.parent)


if __name__ == "__main__":
    va = Vertex('a')
    vb = Vertex('b')
    vh = Vertex('h')
    vc = Vertex('c')
    vi = Vertex('i')
    vg = Vertex('g')
    vf = Vertex('f')
    ve = Vertex('e')
    vd = Vertex('d')

    va.adj_vertexes = [(4, vb), (8, vh)]
    vb.adj_vertexes = [(4, va), (11, vh), (8, vc)]
    vc.adj_vertexes = [(8, vb), (7, vd), (2, vi), (4, vf)]
    vd.adj_vertexes = [(7, vc), (9, ve), (14, vf)]
    ve.adj_vertexes = [(9, vd), (10, vf)]
    vf.adj_vertexes = [(4, vc), (2, vg), (14, vd), (10, ve)]
    vg.adj_vertexes = [(1, vh), (6, vi), (2, vf)]
    vh.adj_vertexes = [(8, va), (11, vb), (7, vi), (1, vg)]
    vi.adj_vertexes = [(7, vh), (6, vg), (2, vc)]

    '''
    edges = [(4, (va, vb)), (8, (va, vh)), (11, (vb, vh)), (8, (vb, vc)),
             (2, (vc, vi)), (4, (vc, vf)), (7, (vc, vd)), (9, (vd, ve)),
             (14, (vd, vf)), (10, (ve, vf)), (2, (vf, vg)), (6, (vg, vi)),
             (1, (vg, vh)), (7, (vh, vi))]
    MST_edges = min_spanning_tree(edges)
    print(MST_edges)
    '''
    graph = [va, vb, vc, vd, ve, vf, vg, vh, vi]
    MST(graph)
    walk_MST(graph)
    
