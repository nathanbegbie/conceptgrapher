import regex as re
from Graph import Graph
from Group import Group
from Nodes import FactNode, ConceptNode, MisconNode, ScaseNode
# from Edge import Edge


class Translator:

    def initialise_data(self):
        print "hello!"
        # create the graph
        graph = Graph()

        # get the file
        f = open('FinancialMaths.map', 'r')

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
                print "Unkown data type"

        print graph.numNodes

        # add the edges

        
