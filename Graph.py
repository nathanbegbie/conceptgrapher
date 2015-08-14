class Graph(object):
    """A graph of nodes and edges

    Attributes:
        nodes: a dictionary of the nodes objects contained
        edges: a dictionary of edges connecting the nodes
        numNodes: integer of how many nodes in the graph
    """

# group should be subclass :(

    def __init__(self, nodes={}, edges=[], groups={}):
        self.nodeDict = nodes
        self.edgeArray = edges
        self.groupDict = groups
        self.numNodes = len(self.nodeDict)

    # need add_group_node etc? The node itself will be the correct node type
    def add_node(self, node):
        self.nodeDict[node.ID] = node
        self.numNodes += 1

    def remove_node(self, node):
        if self.nodeDict[node.ID]:
            del self.nodeDict[node.ID]

    def add_edge(self, edge):
        self.edgeArray.append(edge)

    def remove_edge(self, sourceID, targetID):
        for i in range(0, len(self.edgeArray)):
            if ((self.edgeArray[i].source == sourceID) and
                    (self.edgeArray[i].target == targetID)):
                del self.edgeArray[i]
                break

    def add_group(self, group):
        self.groupDict[group.groupID] = group

    def remove_group(self, group):
        if self.groupDict[group.groupID]:
            del self.groupDict[group.groupID]

    def export(self, filename):
        # export the graph to JSON file
        pass
