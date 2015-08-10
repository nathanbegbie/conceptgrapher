class Group(object):
    """A group of nodes

    Attributes:
        groupID: unique identifier of group
        colour: colour in which the nodes of that group will be displayed
    """

    def __init__(self, groupID):
        self.groupID = groupID