class Node(object):
    """A node of the graph

    Attributes:
        ID: a string representing the Node's ID (unique identifier).
        label: a string representing the Node's description
        colour
        shape
        groups: a list of strings representing the groups to which the node belongs     #dictionary?
        ?inDegree: an integer of how many edges point to the node
        ?outDegree: an integer of how many nodes the node points to                     #just len(successors)
        successors: A list of Node objects one edge away from the node                  #dictionary
    """

    def __init__(self, ID, label):
        """Return a Node object with name *name* and label *label*"""
        self.ID = ID
        self.label = label
        self.colour = "black"
        self.shape = "circle"
        self.successors = {}
        self.outDegree = 0

    def add_group(group): #group object??

    def add_successor(node):
       self.successors[node.ID] = node


        