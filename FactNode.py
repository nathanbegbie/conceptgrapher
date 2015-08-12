from Node import Node


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
