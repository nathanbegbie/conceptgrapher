import sys
import os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from Nodes import Node
from Graph import Graph
from Edge import Edge


class TestGraph:
    def test_empty_graph_creation(self):
        test_graph = Graph()
        assert test_graph.nodeDict == {}
        assert test_graph.edgeDict == {}
        assert test_graph.groupDict == {}

    def test_graph_creation_with_node(self):
        test_node = Node("id1234", "test label")
        node_dict = {test_node.ID: test_node}
        test_graph = Graph(nodes=node_dict)
        assert test_graph.nodeDict == {"id1234": test_node}

    def test_graph_creation_with_edge(self):
        test_edge = Edge('1234', '5678')
        edge_dict = {test_edge.source: test_edge}
        test_graph = Graph(edges=edge_dict)
        assert test_graph.edgeDict == edge_dict
        assert test_graph.edgeDict['1234'] == test_edge
        assert test_graph.edgeDict['1234'].targets == ['5678']

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

    def test_edge_removal(self):
        test_graph1 = Graph()
        assert test_graph1.edgeDict == {}
        test_graph1.add_edge('1234', '5678')
        test_graph1.add_edge('1234', 'abc')
        test_graph1.add_edge('foo', 'bar')
        assert '1234' in test_graph1.edgeDict
        assert test_graph1.edgeDict['1234'].targets == ['5678', 'abc']
        test_graph1.remove_edge("1234", "5678")
        assert '1234' in test_graph1.edgeDict
        assert test_graph1.edgeDict['1234'].targets == ['abc']
        test_graph1.remove_edge("1234", "abc")
        assert '1234' not in test_graph1.edgeDict
        assert 'foo' in test_graph1.edgeDict
        # test source is not there - no error
        test_graph1.remove_edge("nonexistant", "5678")
        # test destination is not there - no error
        test_graph1.remove_edge("foo", "nonexistant")

        test_graph1.remove_edge('foo', 'bar')
        assert 'foo' not in test_graph1.edgeDict
        assert test_graph1.edgeDict == {}

    def test_edge_addition(self):
        test_graph = Graph()
        test_graph.add_edge('1234', '5678')
        test_graph.add_edge('1234', 'abc')
        test_graph.add_edge('foo', 'bar')
        assert '1234' in test_graph.edgeDict
        assert 'foo' in test_graph.edgeDict
        assert test_graph.edgeDict['1234'].targets == ['5678', 'abc']
        assert test_graph.edgeDict['foo'].targets == ['bar']
        del test_graph
