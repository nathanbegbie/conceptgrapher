from Graph import Graph
from Nodes import Node

class Cycles:
        def my_scc(graph):
        index_counter = [0]
        stack = []
        lowlinks = {}
        index = {}
        result = []

        def strongconnect(nodeID):
            # set the depth index for this node to the smallest unused index
            index[nodeID] = index_counter[0]
            lowlinks[nodeID] = index_counter[0]
            index_counter[0] += 1
            stack.append(nodeID)

            # Consider successors of `node`
            for successorID in graph.nodeDict[nodeID].successors.iterkeys():
                if successorID not in lowlinks:
                    # Successor has not yet been visited; recurse on it
                    strongconnect(successorID)
                    lowlinks[nodeID] = min(lowlinks[nodeID], lowlinks[successorID])
                elif successorID in stack:
                    # the successor is in the stack and hence in the current SCC
                    lowlinks[nodeID] = min(lowlinks[nodeID], index[successorID])

            # If `node` is a root node, pop the stack and generate an SCC
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
            if nodeID not in lowlinks:
                strongconnect(nodeID)

        return result
