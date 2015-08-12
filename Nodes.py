class Node(object):
    """A node of the graph

    Attributes:
        ID: a string representing the Node's ID (unique identifier).
        label: a string representing the Node's description
        colour
        shape
        groups: a list of strings of the groups to which the node belongs
        ?inDegree: an integer of how many edges point to the node
        ?outDegree: an integer of how many nodes the node points to
        successors: A list of Node objects one edge away from the node
    """

    def __init__(self, ID, label):
        """Return a Node object with name *name* and label *label*"""
        self.ID = ID
        self.label = label
        self.colour = "black"
        self.shape = "circle"
        self.successors = {}
        self.outDegree = 0

    # def add_group(group):

    def add_successor(self, node):
        self.successors[node.ID] = node


class FactNode(Node):
    """A subclass of Node, specifically a node containing a fact.
Attributes
    :
    content: a string containing the content of the fact
    """

    def __init__(self, ID, label, content):
        """Return a Node object with name *name* and label *label*"""
        # super?
        self.ID = ID
        self.label = label
        self.content = content


class MisconNode(Node):
    """A subclass of Node, specifically a node containing a misconception.

    Attributes:
    content: a string containing the content of the misconception
    """

    def __init__(self, ID, label, content):
        """Return a Node object with name *name* and label *label*"""
        self.ID = ID
        self.label = label
        self.content = content


class ScaseNode(Node):
    """A subclass of Node, specifically a node containing an scase.

    Attributes:
    content: a string containing the content of the scase
    """

    def __init__(self, ID, label, content):
        """Return a Node object with name *name* and label *label*"""
        self.ID = ID
        self.label = label
        self.content = content


class ConceptNode(Node):
    """A subclass of Node, specifically a node containing a concept.

    Attributes:
    content: a string containing the content of the concept
    """

    def __init__(self, ID, label, content):
        """Return a Node object with name *name* and label *label*"""
        self.ID = ID
        self.label = label
        self.content = content
        