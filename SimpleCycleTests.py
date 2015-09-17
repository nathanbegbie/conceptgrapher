from Graph import Graph
from Nodes import Node
from Nodes import FactNode
from Nodes import ConceptNode
from Nodes import MisconNode
from Nodes import ScaseNode
from Cycles import Cycles


class SimpleDoingStuff:
    def single_cycle():
        graph = Graph()
        nodeA = FactNode(ID="A", label="node")
        nodeB = ConceptNode(ID="B", label="node")
        nodeC = FactNode(ID="C", label="node")
        nodeA.add_successor(nodeB)
        nodeB.add_successor(nodeC)
        nodeC.add_successor(nodeA)
        graph.add_node(nodeA)
        graph.add_node(nodeB)
        graph.add_node(nodeC)
        assert Cycles().find_cycle(graph) == [('C', 'B', 'A')]

    def two_cycles():
        graph = Graph()
        nodeA = Node(ID="A", label="node")
        nodeB = Node(ID="B", label="node")
        nodeC = Node(ID="C", label="node")
        nodeD = Node(ID="D", label="node")
        nodeE = Node(ID="E", label="node")
        nodeF = Node(ID="F", label="node")
        nodeA.add_successor(nodeB)
        nodeB.add_successor(nodeC)
        nodeC.add_successor(nodeA)
        nodeD.add_successor(nodeE)
        nodeE.add_successor(nodeF)
        nodeF.add_successor(nodeD)
        graph.add_node(nodeA)
        graph.add_node(nodeB)
        graph.add_node(nodeC)
        graph.add_node(nodeD)
        graph.add_node(nodeE)
        graph.add_node(nodeF)
        assert Cycles().find_cycle(graph) == [('C', 'B', 'A'), ('D', 'F', 'E')]

    def overlapping_cycles():
        graph = Graph()
        nodeA = Node(ID="A", label="node")
        nodeB = Node(ID="B", label="node")
        nodeC = Node(ID="C", label="node")
        nodeD = Node(ID="D", label="node")
        nodeE = Node(ID="E", label="node")
        nodeA.add_successor(nodeB)
        nodeB.add_successor(nodeC)
        nodeC.add_successor(nodeA)
        nodeC.add_successor(nodeE)
        nodeE.add_successor(nodeD)
        nodeD.add_successor(nodeB)
        graph.add_node(nodeA)
        graph.add_node(nodeB)
        graph.add_node(nodeC)
        graph.add_node(nodeD)
        graph.add_node(nodeE)
        assert Cycles().find_cycle(graph) == [('C', 'B', 'A'), ('D', 'E', 'C', 'B')]

    def no_cycles():
        graph = Graph()
        nodeA = FactNode(ID="A", label="nodeA")
        nodeB = MisconNode(ID="B", label="nodeB")
        nodeC = FactNode(ID="C", label="nodeC")
        nodeA.add_successor(nodeB)
        nodeA.add_successor(nodeC)
        nodeB.add_successor(nodeC)
        graph.add_node(nodeA)
        graph.add_node(nodeB)
        graph.add_node(nodeC)
        assert Cycles().find_cycle(graph) == []

    def medium_graph():
        graph = Graph()
        nodeA = Node(ID="A", label="node")
        nodeB = Node(ID="B", label="node")
        nodeC = Node(ID="C", label="node")
        nodeD = Node(ID="D", label="node")
        nodeE = Node(ID="E", label="node")
        nodeF = Node(ID="F", label="node")
        nodeA.add_successor(nodeB)
        nodeB.add_successor(nodeC)
        nodeB.add_successor(nodeD)
        nodeC.add_successor(nodeA)
        nodeC.add_successor(nodeE)
        nodeF.add_successor(nodeB)
        graph.add_node(nodeA)
        graph.add_node(nodeB)
        graph.add_node(nodeC)
        graph.add_node(nodeD)
        graph.add_node(nodeE)
        graph.add_node(nodeF)
        assert Cycles().find_cycle(graph) == [('C', 'B', 'A')]

    # single_cycle()
    # two_cycles()
    # overlapping_cycles() #fails
    # no_cycles()
    # medium_graph()
