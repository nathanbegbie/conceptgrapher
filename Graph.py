class Graph(object):
    """A graph of nodes and edges

    Attributes:
        nodes: a dictionary of the nodes objects contained
        edges: a dictionary of edges connecting the nodes
        numNodes: integer of how many nodes in the graph
        
    """

#group should be subclass :(

    def __init__():
    	self.nodeDict = {}
    	self.edgeDict = {}
    	numNodes = 0


    def __init__(self, nodes, edges): #nodes, edges are dictionaries
        self.nodeDict = nodes
        self.edgeDict = edges
        numNodes = len(nodes)


    #need add_group_node etc? The node itself will be the correct node type
    def add_node(node):
    	self.nodeDict[node.ID] = node
    	numNodes++

    def remove_node(node):
    	del self.nodeDict[node.ID]

   	def add_edge(edge):
   		edgeDict[edge.nodeFrom.ID] = edge

   	def remove_edge(edge):
   		del edgeDict[edge.nodeFrom.ID]

   	def export(fileName):
   		#eport the graph to JSON file

