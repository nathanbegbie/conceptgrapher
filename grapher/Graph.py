from Edge import Edge


class Graph(object):
    """A graph of nodes and edges

    Attributes:
        nodes: a dictionary of the nodes objects contained
        edges: a dictionary of edges connecting the nodes
        numNodes: integer of how many nodes in the graph
    """

# group should be subclass :(

    def __init__(self, nodes={}, edges={}, groups={}):
        self.nodeDict = nodes
        self.edgeDict = edges
        self.groupDict = groups
        self.numNodes = len(self.nodeDict)

    # need add_group_node etc? The node itself will be the correct node type
    def add_node(self, node):
        self.nodeDict[node.ID] = node
        self.numNodes += 1

    def remove_node(self, node):
        if self.nodeDict[node.ID]:
            del self.nodeDict[node.ID]

    def add_edge(self, sourceID, targetID):
        # check if edge exists
        if sourceID in self.edgeDict:
            self.edgeDict[sourceID].targets.append(targetID)
        else:
            self.edgeDict[sourceID] = Edge(sourceID, targetID)

    def remove_edge(self, sourceID, targetID):
        # check source exists
        if sourceID in self.edgeDict:
            # check that source has the code
            if targetID in self.edgeDict[sourceID].targets:
                self.edgeDict[sourceID].targets.remove(targetID)
                if len(self.edgeDict[sourceID].targets) == 0:
                    print "deleting"
                    del self.edgeDict[sourceID]
            else:
                print "Target does not exist"
        else:
            print "Source does not exist"

    def add_group(self, group):
        self.groupDict[group.groupID] = group

    def remove_group(self, group):
        if self.groupDict[group.groupID]:
            del self.groupDict[group.groupID]

    def export(self, filename):
        # export the graph to JSON file
        pass
