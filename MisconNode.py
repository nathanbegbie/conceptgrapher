from Node import Node


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
