class ConceptNode(Node):
	 """A subclass of Node, specifically a node containing a concept.

    Attributes:
    content: a string containing the content of the fact
    """

    def __init__(self, name, label, content):
    	self.name = name
    	self.label = label
    	self.content = content