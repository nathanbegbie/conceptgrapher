class Graph(object):
    """A graph of nodes and edges

    Attributes:
        nodes: a list of the nodes objects contained
        edges: a list of edges connecting the nodes
        numNodes: integer of how many nodes in the graph
        
    """

    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges