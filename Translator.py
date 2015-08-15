import regex as re
from Graph import Graph
from Group import Group
from Nodes import FactNode, ConceptNode, MisconNode, ScaseNode
import json
import random


class Translator:

    def initialise_data(self):
        print "hello!"
        # create the graph
        graph = Graph()

        # get the file
        try:
            f = open('FinancialMaths.map', 'r')
        except IOError:
            print "file read error"

        # get the first set of the groups
        map_file = f.read()
        f.close()

        # get all lines with node format
        node_dict = (re.findall(
            r'[A-z]{4}\d{3,4}\s*\[.*type=\".*\".*label=\".*\".*]',
            map_file))

        # get all nodes with info between /* and */
        node_dict += (re.findall(
            r'[A-z]{4}\d{3,4}\s?/\*.*\*/',
            map_file,
            re.I | re.M))

        for node in node_dict:
            # get the id
            id = re.match(r'[A-z]{4}\d{3,4}', node)[0]
            type = re.search(r'type=\".*\",', node)[0][6:-2]
            label = re.search(r',\slabel=\".*\"', node)[0][9:-1]

            if(type == "group"):
                graph.add_group(Group(groupID=id, content=label))
            elif(type == "fact"):
                graph.add_node(FactNode(ID=id, content=label))
            elif(type == "concept"):
                graph.add_node(ConceptNode(ID=id, content=label))
            elif(type == "miscon"):
                graph.add_node(MisconNode(ID=id, content=label))
            elif(type == "scase"):
                graph.add_node(ScaseNode(ID=id, content=label))
            else:
                print "Unknown data type"

        print graph.numNodes

        # add the edges
        edge_dict = (re.findall(
            r'[A-z]{4}\d{3,4}\s?->\s?[A-z]{4}\d{3,4}',
            map_file, overlapped=True))
        # edge cases
        edge_dict += (re.findall(
            r'[A-z]{3,4}\d{3,4}\s?/\*.*\*/\s?->\s?[A-z]{4}\d{3,4}',
            map_file))

        for edge in edge_dict:
            codes = re.findall(r'[A-z]{3,4}\d{3,4}', edge)
            graph.add_edge(codes[0], codes[1])

        print len(graph.nodeDict)

        # create the array of node dict
        nodes = []
        # iterate through the nodes
        for key, value in graph.nodeDict.iteritems():
            nodes.append({"name": value.ID,
                          "group": str(random.randint(1, 5))})

        print len(nodes)

        links = []
        for i in range(0, len(nodes)):
            # see if the node has any edges
            # get the id of the graph, check if it is in the dict of edges
            source_id = nodes[i]["name"]

            if source_id in graph.edgeDict:
                # iterate through the list of targets
                # for each target, get target's position in the nodes array
                for target_id in graph.edgeDict[source_id].targets:
                    position = 0
                    for j in range(0, len(nodes)):
                        # check if we have found the position of the node
                        if target_id == nodes[j]["name"]:
                            position = j
                            break
                    links.append({"source": i, "target": position})
            else:
                print "node " + source_id + " has no edges"
        data = {"nodes": nodes, "links": links}
        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)
