from Nodes import Node
from Graph import Graph
from Edge import Edge


class TestGraph:
    def test_empty_graph_creation(self):
        test_graph = Graph()
        assert test_graph.nodeDict == {}
        assert test_graph.edgeArray == []
        assert test_graph.groupDict == {}

    def test_graph_creation_with_node(self):
        test_node = Node("id1234", "test label")
        node_dict = {test_node.ID: test_node}
        test_graph = Graph(nodes=node_dict)
        assert test_graph.nodeDict == {"id1234": test_node}

    def test_graph_creation_with_edge(self):
        test_edge = Edge('1234', '5678')
        edge_array = [test_edge]
        test_graph = Graph(edges=edge_array)
        assert test_graph.edgeArray == edge_array

    def test_node_addition(self):
        test_node = Node("id1234", "test label")
        test_graph = Graph()
        test_graph.add_node(test_node)
        assert test_graph.nodeDict["id1234"] == test_node

    def test_node_removal(self):
        test_node1 = Node("id1234", "test label 1")
        test_node2 = Node("id5678", "test label 2")
        node_dict = {test_node1.ID: test_node1, test_node2.ID: test_node2}
        test_graph = Graph(nodes=node_dict)
        test_graph.remove_node(test_node1)
        assert test_node1 not in test_graph.nodeDict

    def test_edge_addition(self):
        test_graph = Graph()
        test_edge = Edge('1234', '5678')
        test_graph.add_edge(test_edge)
        assert test_edge in test_graph.edgeArray

    def test_edge_removal(self):
        test_edge1 = Edge("id1234a", "id1234b")
        test_edge2 = Edge("id5678a", "id5678a")
        edge_array = [test_edge1, test_edge2]
        test_graph = Graph(edges=edge_array)
        test_graph.remove_edge("id1234a", "id1234b")
        assert test_edge1 not in test_graph.edgeArray
