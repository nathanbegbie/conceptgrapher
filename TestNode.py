from Nodes import Node, FactNode, ConceptNode, MisconNode, ScaseNode


class TestNode:

    def test_node_creation(self):
        test_node = Node("id1234", "test label")
        assert test_node.ID == "id1234"
        assert test_node.label == "test label"

    def test_fact_node_creation(self):
        test_node = FactNode("id1234", "test label", "test fact")
        assert test_node.ID == "id1234"
        assert test_node.label == "test label"
        assert test_node.content == "test fact"

    def test_concept_node_creation(self):
        test_node = ConceptNode("id1234", "test label", "test concept")
        assert test_node.ID == "id1234"
        assert test_node.label == "test label"
        assert test_node.content == "test concept"

    def test_miscon_node_creation(self):
        test_node = MisconNode("id1234", "test label", "test miscon")
        assert test_node.ID == "id1234"
        assert test_node.label == "test label"
        assert test_node.content == "test miscon"

    def test_scase_node_creation(self):
        test_node = ScaseNode("id1234", "test label", "test scase")
        assert test_node.ID == "id1234"
        assert test_node.label == "test label"
        assert test_node.content == "test scase"
