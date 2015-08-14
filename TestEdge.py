from Edge import Edge


class TestEdge:

    def test_edge_creation(self):
        test_edge = Edge("id1234", "id5678")
        assert test_edge.source == "id1234"
        assert test_edge.target == "id5678"
