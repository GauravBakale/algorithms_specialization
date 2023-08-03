# Graph class

class Vertex:
    """
        Create a node or vertex that can be used as tail or head in an edge. 
    """
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class Edge:
    """
        Create a edge. This is a directed edge and if undirected edge is required 2 must be manually created.
    """
    def __init__(self, source_vertex : Vertex, destination_vertex:Vertex, weight:int = 1, undirected:bool = True):
        self.source_vertex = source_vertex
        self.destination_vertex = destination_vertex
        self.name = source_vertex.name + '-' + destination_vertex.name
        self.undirected = undirected
        self.weight = weight

    def get_weight(self):
        return self.weight
    
    def get_source(self):
        return self.source_vertex

    def get_destination(self):
        return self.destination_vertex
    
    def __str__(self):
        if self.undirected:
            return f"{self.source_vertex} <--> {self.destination_vertex}"
        else:
            return f"{self.source_vertex} --> {self.destination_vertex}"
    
    def __repr__(self):
        if self.undirected:
            return f"{self.source_vertex} <--> {self.destination_vertex}"
        else:
            return f"{self.source_vertex} --> {self.destination_vertex}"

class Graph:

    """
        Create a Graph with vertexes and edges
    """

    def __init__(self, name: str, undirected=False):
        self.name = name
        self.undirected = undirected
        self.vertexes = {}
        self.edges = {}
        self.all_edges = {}

    def add_vertex(self, vertex:str):
        V = Vertex(vertex)
        if vertex in self.vertexes.keys():
            raise Exception(f"Vertex '{vertex}' is already a part of the graph")
        self.vertexes[vertex]=V
    
    def list_vertexes(self):
        print(f"verteces: {list(self.vertexes.keys())}")

    def drop_vertex(self, vertex:str):
        if vertex not in self.vertexes.keys():
            raise Exception(f"Vertex '{vertex}' not found")
        self.vertexes.pop(vertex)

    def add_edge(self, source_vertex: str , destination_vertex: str, weight:int = 1):

        E = Edge(
            self.vertexes[source_vertex], 
            self.vertexes[destination_vertex],
            weight,
            self.undirected
        )
        if E.name in self.all_edges.keys():
            raise ValueError(f"Edge '{E}' is already a part of the graph")
        
        self.edges[E.name]=E
        self.all_edges[E.name]=E
        if self.undirected:
            other_edge = Edge(
                self.vertexes[destination_vertex],
                self.vertexes[source_vertex],
                self.undirected
            )
            self.all_edges[other_edge.name] = other_edge
    
    def list_edges(self):
        for edge_name in self.all_edges:
            print(f"edges: {self.all_edges[edge_name]}, [{self.all_edges[edge_name].get_weight()}]")

    def drop_edge(self, edge_name):
        try: 
            E = self.edges[edge_name]
            edge_name = E.source_vertex.name + "-" + E.destination_vertex.name
            # remove the edge from normal list
            self.edges.pop(edge_name)
            # remove the edges from all edges list
            self.all_edges.pop(edge_name)
            
            if self.undirected:
                other_edge_name = E.destination_vertex.name + "-" + E.source_vertex.name
                self.all_edges.pop(other_edge_name)
        except KeyError as e:
            raise Exception(f"Edge {edge_name} not found")
    
    def __str__(self) -> str:
        return self.name
    
    def __repr__(self):
        return f"{self.name}"

# create a graph with lists of vertexes and nodes
def create_graph(graph_name,vertexes, edges, weights = [],undirected=False):
    """
        Create a graph object.
        Usage:
            I/P : 
                nodes = "a,b,c,d,e,f,g,h"
                edges = "a-b,a-e,b-e,b-c,c-d,d-e,e-f,e-g,f-g,g-h"
            create_graph("G", nodes, edges, False)
    """
    G = Graph(graph_name, undirected)
    
    vertexes = vertexes.split(',')
    for vertex in vertexes:
        G.add_vertex(vertex)

    edges = edges.split(',')
    # if the weights are given and the count does not match of edges and weights then raise exception
    if weights:
        weights = [int(i) for i in weights.split(',')]
        if len(weights) != len(edges):
            raise Exception("the length of edges and the weights should match.")
        
    for i in range(len(edges)):
        try:
            edge = edges[i]
            if weights:
                weight = weights[i]
            else:
                weight = 1

            G.add_edge(
                edge.split('-')[0],
                edge.split('-')[1],
                weight
            )
            
        except Exception as e:
            print(e)
    
    G.list_vertexes()
    G.list_edges()
    print("")
    return G

# nodes = "abcdefgh"
# edges = "ab,ae,be,bc,cd,de,ef,eg,fg,gh"
# G = create_graph(nodes,edges)
    
