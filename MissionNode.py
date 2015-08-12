class MissionNode(Node):
	 """A subclass of Node, specifically a node containing a misson.

    Attributes:
    content: a string containing the content of the mission
    """

    def __init__(self, name, label, content):
    	self.name = name
    	self.label = label
    	self.content = content