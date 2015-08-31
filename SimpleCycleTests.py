from Graph import Graph
from Nodes import Node
from Cycles import Cycles


class SimpleDoingStuff:
    def single_cycle():
        #  myCycle = Cycles()
        graph = Graph()
        nodeA = Node(ID="A", label="node")
        nodeB = Node(ID="B", label="node")
        nodeC = Node(ID="C", label="node")
        nodeA.add_successor(nodeB)
        nodeB.add_successor(nodeC)
        nodeC.add_successor(nodeA)
        graph.add_node(nodeA)
        graph.add_node(nodeB)
        graph.add_node(nodeC)
        assert Cycles().find_scc(graph) == [('C', 'B', 'A')]

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
        assert Cycles().find_scc(graph) == [('C', 'B', 'A'), ('D', 'F', 'E')]

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
        assert Cycles().find_scc(graph) == [('C', 'B', 'A'), ('D', 'E', 'C', 'B')]

    single_cycle()
    two_cycles()
    overlapping_cycles()
