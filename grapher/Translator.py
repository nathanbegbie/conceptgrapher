import regex as re
from Graph import Graph
from Group import Group
from Nodes import FactNode, ConceptNode, MisconNode, ScaseNode
import json
from os import pardir, path


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
            raise SystemExit

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
            label = (re.search(r',\slabel=\".*\"', node)[0][9:-1]
                     .replace("\\n", " "))

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

        print "number of nodes", graph.numNodes
        print "number of groups", len(graph.groupDict)

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

        # Get the groups
        group_starts = re.finditer(
            r'([A-z]{4}\d{3,4}|[A-z]{7}\s?\[.*\]\s?)\s?\{',
            map_file)
        # count = 0
        groups = {}
        for item in group_starts:
            # get the name of the group
            group_names = re.findall(
                r'[A-z]{4}\d{3,4}|[A-z]{7}',
                item.group(0))
            group_name = group_names[0]
            # set the start position to the pos of the '{'
            count = item.end()
            # keep track of brackets until we have a matching number
            bracket_count = 1
            while(bracket_count > 0):
                char = map_file[count]
                if char == "{":
                    bracket_count += 1
                elif char == "}":
                    bracket_count -= 1
                else:
                    pass
                count += 1
            # get all of the nodes within the group
            nodes = re.findall(r'[A-z]{4}\d{3,4}',
                               map_file[(item.end() - 1):(count + 1)])
            # get the list of nodes to correspond to the group names
            groups[group_name] = nodes

        # CREATE THE JSON
        # create the array of node dict
        nodes = []
        # iterate through the nodes
        for key, value in graph.nodeDict.iteritems():

            typeof = ""
            if isinstance(value, FactNode):
                typeof = "FactNode"
            elif isinstance(value, ConceptNode):
                typeof = "ConceptNode"
            elif isinstance(value, MisconNode):
                typeof = "MisconNode"
            elif isinstance(value, ScaseNode):
                typeof = "ScaseNode"
            else:
                print "Error of Node type"

            nodes_groups = []
            # iterate through each group
            # see if the node belongs to the group
            for group in groups:
                if value.ID in groups[group]:
                    nodes_groups.append(group)

            nodes.append({"name": value.ID,
                          "group": nodes_groups,
                          "typeof": typeof,
                          "content": value.content})

        print len(nodes)

        links = []
        # add the edges
        for source in graph.edgeDict:
            if source in graph.groupDict:
                continue
            for target in graph.edgeDict[source].targets:
                if target in graph.groupDict:
                    continue
                value = graph.nodeDict[target]
                typeof = ""
                if (isinstance(value, FactNode) or
                        isinstance(value, ConceptNode)):
                    typeof = "directed"
                elif (isinstance(value, MisconNode) or
                        isinstance(value, ScaseNode)):
                    typeof = "undirected"
                else:
                    print "Error of Node type"
                links.append({"source": source,
                              "target": target,
                              "typeof": typeof})

        data = {"nodes": nodes, "links": links}

        # set up correct file directory
        mypath = path.dirname(path.realpath(__file__))
        destination_file = (path.join(mypath, pardir) + "/data.json")

        with open(destination_file, 'w') as outfile:
            json.dump(data, outfile, indent=2, sort_keys=True)
