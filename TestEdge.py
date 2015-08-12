from Edge import Edge
from Nodes import Node


class TestEdge:

    def test_edge_creation(self):
        test_node_from = Node("id1234", "from label")
        test_node_to = Node("id5678", "to label")
        test_edge = Edge(test_node_from, test_node_to)
        assert test_edge.nodeFrom.ID == "id1234"
        assert test_edge.nodeTo.ID == "id5678"
        assert test_edge.nodeFrom.label == "from label"
        assert test_edge.nodeTo.label == "to label"
