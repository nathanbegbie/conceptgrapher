from Nodes import Node
from Graph import Graph
from Edge import Edge


class TestGraph:
    def test_empty_graph_creation(self):
        test_graph = Graph()
        assert test_graph.nodeDict == {}
        assert test_graph.edgeDict == {}

    def test_graph_creation_with_node(self):
        test_node = Node("id1234", "test label")
        node_dict = {test_node.ID: test_node}
        test_graph = Graph(nodes=node_dict)
        assert test_graph.nodeDict == {"id1234": test_node}

    def test_graph_creation_with_edge(self):
        nFrom = Node("idFrom", "from label")
        nTo = Node("idTo", "to label")
        test_edge = Edge(nFrom, nTo)
        edge_dict = {test_edge.nodeFrom.ID: test_edge}
        test_graph = Graph(edges=edge_dict)
        assert test_graph.edgeDict == {"idFrom": test_edge}

    def test_node_addition(self):
        test_node = Node("id1234", "test label")
        test_graph = Graph()
        test_graph.addNode(test_node)
        assert test_graph.nodeDict["id1234"] == test_node

    def test_node_removal(self):
        test_node1 = Node("id1234", "test label 1")
        test_node2 = Node("id5678", "test label 2")
        node_dict = {test_node1.ID: test_node1, test_node2.ID: test_node2}
        test_graph = Graph(nodes=node_dict)
        test_graph.removeNode(test_node1)
        assert test_graph.nodeDict["id1234"] is None

    def test_edge_addition(self):
        nFrom = Node("idFrom", "from label")
        nTo = Node("idTo", "to label")
        test_edge = Edge(nFrom, nTo)
        test_graph = Graph()
        test_graph.addEdge(test_edge)
        assert test_graph.edgeDict["idFrom"] == test_edge

    def test_edge_removal(self):
        test_node1a = Node("id1234a", "test label 1a")
        test_node1b = Node("id1234b", "test label 1b")
        test_node2a = Node("id5678a", "test label 2a")
        test_node2b = Node("id5678a", "test label 2b")
        test_edge1 = Edge(test_node1a, test_node1b)
        test_edge2 = Edge(test_node2a, test_node2b)
        edge_dict = {test_edge1.nodeFrom.ID: test_edge1,
                     test_edge2.nodeFrom.ID: test_edge2}
        test_graph = Graph(edges=edge_dict)
        test_graph.removeEdge(test_edge1)
        assert test_graph.edgeDict["id1234a"] is None
