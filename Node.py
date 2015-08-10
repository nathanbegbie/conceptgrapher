class Node(object):
    """A node of the graph

    Attributes:
        name: a string representing the Node's name (unique identifier).
        label: a string representing the Node's description
        colour
        shape
        groups: a list of strings representing the groupd to which the node belongs
        ?inDegree: an integer of how many edges point to the node
        ?outDegree: an integer of how many nodes the node points to
        neighbours: A list of Node objects one edge away from the node
    """

    def __init__(self, name, label):
        """Return a Node object with name *name* and label *label*"""
        self.name = name
        self.label = label
        self.colour = "black"
        self.shape = "circle"
        