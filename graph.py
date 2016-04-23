from collections import OrderedDict
class Vertex:
    def __init__(self,key,distance=0,predecessor=None,color="white"):
        self.id = key
        self.connected_to = {}
        self.distance = distance
        self.predecessor = predecessor
        self.color = color
        
    def add_neighbor(self,nbr,weight=0):
        self.connected_to[nbr] = weight
        
    def __str__(self):
        return str(self.id) + ' connected to: ' +str([x.id for x in self.connected_to.keys()])

class Graph:
    def __init__(self):
        self.vertex_list = {}
        self.num_vertices = 0

    def add_vertex(self,key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vertex_list[key] = new_vertex
        return new_vertex

    def get_vertex(self,n):
        if n in self.vertex_list.keys():
            return self.vertex_list[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertex_list.keys()

    def add_edge(self,from_edge,to_edge,cost=0):
        if not from_edge in self.vertex_list.keys():
            nv = self.add_vertex(from_edge)
        if not to_edge in self.vertex_list.keys():
            nv = self.add_vertex(to_edge)
        self.vertex_list[from_edge].add_neighbor(self.vertex_list[to_edge],cost)

    def __iter__(self):
        return iter(self.vertex_list.values())
