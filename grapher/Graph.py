from Edge import Edge


class Graph(object):
    """A graph of nodes and edges

    Attributes:
        nodeDict: a dictionary of the nodes objects contained
        edgeDict: a dictionary of edges connecting the nodes
        groupDict: a dictionary of groups contained in the graph
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
        """add a node to the dictionary of nodes in the graph """
        self.nodeDict[node.ID] = node
        self.numNodes += 1

    def remove_node(self, node):
        """delete a node from the dictionary of nodes in the graph """
        if self.nodeDict[node.ID]:
            del self.nodeDict[node.ID]

    def add_edge(self, sourceID, targetID):
        """add an edge to the dictionary of edges in the graph """
        # check if edge exists
        if (sourceID in self.edgeDict and
                targetID not in self.edgeDict[sourceID].targets):
            self.edgeDict[sourceID].targets.append(targetID)
        else:
            self.edgeDict[sourceID] = Edge(sourceID, targetID)

    def remove_edge(self, sourceID, targetID):
        """remove an edge from the dicitonary of edges in the graph """
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
        """add a group to the dictionary of edges in the graph """
        self.groupDict[group.groupID] = group

    def remove_group(self, group):
        """remove a group from the dictionary of edges in the graph """
        if self.groupDict[group.groupID]:
            del self.groupDict[group.groupID]

    def export(self, filename):
        # export the graph to JSON file
        pass
