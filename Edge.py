# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 16:43:32 2015

@author: jess
"""


class Edge(object):
    """An edge of the graph

    Attributes:
        nodeFrom: node object (origin)
        nodeTo: node object (destination)
        colour: colour of line in visualisation
        thickness: thickness of line in visualisation
    """

    def __init__(self, source, target):
        self.source = source
        self.target = target
