class Edge(object):
    """An edge of the graph

    Attributes:
        targets: list node objects (destination)
        source: node object (origin)
    """

    def __init__(self, source, targets):
        self.targets = []
        self.source = source
        self.targets.append(targets)
