# Graph class

class Vertex:
    """
        Create a node or vertex that can be used as tail or head in an edge. 
    """
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class Edge:
    """
        Create a edge. This is a directed edge and if undirected edge is required 2 must be manually created.
    """
    def __init__(self, source_vertex : Vertex, destination_vertex:Vertex):
        self.source_vertex = source_vertex
        self.destination_vertex = destination_vertex
        self.name = source_vertex.name + '-' + destination_vertex.name
    
    def __str__(self):
        return f"{self.source_vertex} <--> {self.destination_vertex}"
    
    def __repr__(self):
        return f"{self.source_vertex} <--> {self.destination_vertex}"

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

    def add_edge(self, source_vertex: str , destination_vertex: str):

        E = Edge(
            self.vertexes[source_vertex], 
            self.vertexes[destination_vertex]
        )
        if E.name in self.all_edges.keys():
            raise ValueError(f"Edge '{E}' is already a part of the graph")
        
        self.edges[E.name]=E
        self.all_edges[E.name]=E
        if self.undirected:
            other_edge = Edge(
                self.vertexes[destination_vertex],
                self.vertexes[source_vertex],
            )
            self.all_edges[other_edge.name] = other_edge
    
    def list_edges(self):
        print(f"edges: {list(self.edges.keys())}")

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
def create_graph(graph_name,vertexes, edges, undirected=False):
    """
        Create a graph object.
        Usage:
            I/P : 
                nodes = "a,b,c,d,e,f,g,h"
                edges = "a-b,a-e,b-e,b-c,c-d,d-e,e-f,e-g,f-g,g-h"
            create_graph("G", nodes, edges, False)
    """
    G = Graph(graph_name, undirected)
    for vertex in vertexes.split(','):
        G.add_vertex(vertex)
    for edge in edges.split(','):
        try:
            G.add_edge(edge.split('-')[0], edge.split('-')[1])
        except ValueError as e:
            print(e)
    
    G.list_vertexes()
    G.list_edges()
    print("")
    return G

# nodes = "abcdefgh"
# edges = "ab,ae,be,bc,cd,de,ef,eg,fg,gh"
# G = create_graph(nodes,edges)
    
