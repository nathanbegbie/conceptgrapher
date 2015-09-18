class Node(object):
    """A node of the graph

    Attributes:
        ID: a string representing the Node's ID (unique identifier).
        content: a string representing the Node's description
        colour
        shape
        groups: a list of strings of the groups to which the node belongs
        ?inDegree: an integer of how many edges point to the node
        ?outDegree: an integer of how many nodes the node points to
        successors: A list of Node objects one edge away from the node
    """

    def __init__(self, ID, content):
        """Return a Node object with name *name* and content *content*"""
        self.ID = ID
        self.content = content
        self.successors = {}

    def add_successor(self, node):
        self.successors[node.ID] = node


class FactNode(Node):
    """A subclass of Node, specifically a node containing a fact.
Attributes
    :
    content: a string containing the content of the fact
    """

    def __init__(self, ID, content):
        """Return a Node object with name *name* and content *content*"""
        # super?
        self.ID = ID
        self.content = content
        self.successors = {}


class MisconNode(Node):
    """A subclass of Node, specifically a node containing a misconception.

    Attributes:
    content: a string containing the content of the misconception
    """

    def __init__(self, ID, content):
        """Return a Node object with name *name* and content *content*"""
        self.ID = ID
        self.content = content
        self.successors = {}


class ScaseNode(Node):
    """A subclass of Node, specifically a node containing an scase.

    Attributes:
    content: a string containing the content of the scase
    """

    def __init__(self, ID, content):
        """Return a Node object with name *name* and content *content*"""
        self.ID = ID
        self.content = content
        self.successors = {}


class ConceptNode(Node):
    """A subclass of Node, specifically a node containing a concept.

    Attributes:
    content: a string containing the content of the concept
    """

    def __init__(self, ID, content):
        """Return a Node object with name *name* and content *content*"""
        self.ID = ID
        self.content = content
        self.successors = {}
