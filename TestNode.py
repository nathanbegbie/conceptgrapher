from Nodes import Node


class TestNode:

    def test_node_creation(self):
        test_node = Node("id1234", "test label")
        assert test_node.ID == "id1234"
        assert test_node.label == "test label"

    def test_sub_node_creation(self, type):
        test_node = Node("id1234", "test label", "test " + type)
        assert test_node.ID == "id1234"
        assert test_node.label == "test label"
        assert test_node.content == "test " + type

    def test_fact_node_creation(self):
        test_sub_node_creation("fact")

    def test_concept_node_creation(self):
        test_sub_node_creation("concept")

    def test_miscon_node_creation(self):
        test_sub_node_creation("miscon")

    def test_scase_node_creation(self):
        test_sub_node_creation("scase")
