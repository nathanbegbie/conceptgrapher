import Nodes
from Graph import Graph


class Cycles:

    def find_cycle(self, graph):

        index_counter = [0]
        stack = []  # stack of Node IDs
        lowlinks = {}  # to keep track of which nodes have been visited recursively
        index = {}  # key=NodeID, value=integer
        result = []  # list of cycles

        def strongconnect(nodeID):
            # set the depth index for this node to the smallest unused index
            index[nodeID] = index_counter[0]
            lowlinks[nodeID] = index_counter[0]
            index_counter[0] += 1
            stack.append(nodeID)

            # visit successors of the node
            for successorID in graph.nodeDict[nodeID].successors.iterkeys():
                if successorID not in lowlinks:
                    # Successor has not yet been visited; recurse on it
                    strongconnect(successorID)
                    lowlinks[nodeID] = min(lowlinks[nodeID], lowlinks[successorID])
                elif successorID in stack:
                    # the successor is in the stack and so in the current SCC (cycle)
                    lowlinks[nodeID] = min(lowlinks[nodeID], index[successorID])

            # If the node is a root node, pop the stack and start a SCC'
            if lowlinks[nodeID] == index[nodeID]:
                connected_component = []

                while True:
                    successorID = stack.pop()
                    connected_component.append(successorID)
                    if successorID == nodeID:
                        break
                component = tuple(connected_component)
                # storing the result
                result.append(component)

        for nodeID in graph.nodeDict.iterkeys():
            # only visit fact and concept nodes
            if nodeID not in lowlinks:
                strongconnect(nodeID)

        return result
