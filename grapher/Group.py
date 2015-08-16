class Group(object):
    """A group of nodes

    Attributes:
        groupID: unique identifier of group
        nodesInGroup : a dictionary of nodes belonging to the group
        colour: colour in which the nodes of that group will be displayed
    """

    def __init__(self, groupID, content=""):
        self.groupID = groupID
        self.content = content
        self.nodesInGroup = {}

    def add_node_to_group(self, node):
        self.nodesInGroup[node.ID] = node
