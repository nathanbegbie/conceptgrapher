from Nodes import Node, FactNode, ConceptNode, MisconNode, ScaseNode


class TestNode:

    def test_node_creation(self):
        test_node = Node("id1234", "test label")
        assert test_node.ID == "id1234"
        assert test_node.content == "test label"
        assert test_node.successors == {}
        successor_node = Node("id567", "test label")
        test_node.add_successor(successor_node)
        assert len(test_node.successors) == 1
        assert test_node.successors["id567"] == successor_node

    def test_fact_node_creation(self):
        test_node = FactNode("id1234", "test fact")
        assert test_node.ID == "id1234"
        assert test_node.content == "test fact"
        assert test_node.successors == {}
        successor_node1 = Node("id567", "test label")
        test_node.add_successor(successor_node1)
        assert len(test_node.successors) == 1
        assert test_node.successors["id567"] == successor_node1
        successor_node2 = FactNode("id890", "test label")
        test_node.add_successor(successor_node2)
        assert len(test_node.successors) == 2
        assert test_node.successors["id890"] == successor_node2

    def test_concept_node_creation(self):
        test_node = ConceptNode("id1234", "test concept")
        assert test_node.ID == "id1234"
        assert test_node.content == "test concept"
        assert test_node.successors == {}
        successor_node1 = Node("id567", "test label")
        test_node.add_successor(successor_node1)
        assert len(test_node.successors) == 1
        assert test_node.successors["id567"] == successor_node1
        successor_node2 = FactNode("id890", "test label")
        test_node.add_successor(successor_node2)
        assert len(test_node.successors) == 2
        assert test_node.successors["id890"] == successor_node2

    def test_miscon_node_creation(self):
        test_node = MisconNode("id1234", "test miscon")
        assert test_node.ID == "id1234"
        assert test_node.content == "test miscon"
        assert test_node.successors == {}
        successor_node1 = Node("id567", "test label")
        test_node.add_successor(successor_node1)
        assert len(test_node.successors) == 1
        assert test_node.successors["id567"] == successor_node1
        successor_node2 = FactNode("id890", "test label")
        test_node.add_successor(successor_node2)
        assert len(test_node.successors) == 2
        assert test_node.successors["id890"] == successor_node2

    def test_scase_node_creation(self):
        test_node = ScaseNode("id1234", "test scase")
        assert test_node.ID == "id1234"
        assert test_node.content == "test scase"
        assert test_node.successors == {}
        successor_node1 = Node("id567", "test label")
        test_node.add_successor(successor_node1)
        assert len(test_node.successors) == 1
        assert test_node.successors["id567"] == successor_node1
        successor_node2 = FactNode("id890", "test label")
        test_node.add_successor(successor_node2)
        assert len(test_node.successors) == 2
        assert test_node.successors["id890"] == successor_node2
