from Nodes import Node
from Graph import Graph


# a single test
def test_node_creation():
    test_node = Node("id1234", "test label")
    assert test_node.ID == "id1234"
    assert test_node.label == "test label"


# But it's better to create test class that tests specific functionality
class TestGraph:
    def test_empty_graph_creation(self):
        test_graph = Graph()
        assert test_graph.nodeDict == {}
        assert test_graph.edgeDict == {}

    def test_graph_creation_with_input(self):
        test_node = Node("id1234", "test label")
        node_list = {test_node.ID: test_node}
        test_graph = Graph(nodes=node_list)
        assert test_graph.nodeDict == {"id1234": test_node}
