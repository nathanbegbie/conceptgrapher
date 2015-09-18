import regex as re
from Graph import Graph
from Group import Group
from Nodes import FactNode, ConceptNode, MisconNode, ScaseNode
import json
from os import pardir, path, listdir
from os.path import isfile, join


class Translator:
    def __init__(self):
        """constructor which creates graph to store data
        and arrays to store formatted data that is
        transferred to the JSON file"""
        self.graph = Graph()
        # Arrays for JSON data creation
        self.links = []
        self.nodes = []
        self.groups = {}

    def process_data(self):
        """Reads in the .map file and
        stores the information in the appropriate object"""
        # get a list of the files in the directory

        # change to an optional on creation of translator arg
        testing = True

        mypath = path.dirname(path.realpath(__file__))

        print mypath

        destination_directory = path.join(mypath, pardir)

        print destination_directory

        list_of_files = []
        if testing:
            list_of_files = [f for f in ["test1.map", "test2.map"]
                             if isfile(join(destination_directory, f))]
        else:
            list_of_files = [f for f in listdir(destination_directory)
                             if isfile(join(destination_directory, f))]

        for thing in list_of_files:
            print thing

        map_file = ""

        for file_name in list_of_files:
            if (file_name.endswith('.map')):
                # get the file
                try:
                    f = open(join(destination_directory, file_name), "r")
                    map_file += f.read()
                    map_file += "\n"
                    f.close()
                except IOError:
                    print "file read error"
                    raise SystemExit

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
                self.graph.add_group(Group(groupID=id, content=label))
            elif(type == "fact"):
                self.graph.add_node(FactNode(ID=id, content=label))
            elif(type == "concept"):
                self.graph.add_node(ConceptNode(ID=id, content=label))
            elif(type == "miscon"):
                self.graph.add_node(MisconNode(ID=id, content=label))
            elif(type == "scase"):
                self.graph.add_node(ScaseNode(ID=id, content=label))
            else:
                print "Unknown data type"

        print "number of nodes", self.graph.numNodes
        print "number of groups", len(self.graph.groupDict)

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
            self.graph.add_edge(codes[0], codes[1])

        print len(self.graph.nodeDict)

        # Get the groups
        group_starts = re.finditer(
            r'([A-z]{4}\d{3,4}|[A-z]{7}\s?\[.*\]\s?)\s?\{',
            map_file)
        # count = 0

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
            self.nodes = re.findall(r'[A-z]{4}\d{3,4}',
                                    map_file[(item.end() - 1):(count + 1)])
            # get the list of nodes to correspond to the group names
            self.groups[group_name] = self.nodes

    def output_data(self):
        """This takes the information stored in the objects and
        outputs a json file with the appropriate data"""
        for key, value in self.graph.nodeDict.iteritems():
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
            for group in self.groups:
                if value.ID in self.groups[group]:
                    nodes_groups.append(group)

            self.nodes.append({"name": value.ID,
                               "group": nodes_groups,
                               "typeof": typeof,
                               "content": value.content})

        print len(self.nodes)

        # add the edges
        for source in self.graph.edgeDict:
            if source in self.graph.groupDict:
                continue
            for target in self.graph.edgeDict[source].targets:
                if target in self.graph.groupDict:
                    continue
                value = self.graph.nodeDict[target]
                typeof = ""
                if (isinstance(value, FactNode) or
                        isinstance(value, ConceptNode)):
                    typeof = "directed"
                elif (isinstance(value, MisconNode) or
                        isinstance(value, ScaseNode)):
                    typeof = "undirected"
                else:
                    print "Error of Node type"
                self.links.append({"source": source,
                                   "target": target,
                                   "typeof": typeof})

        data = {"nodes": self.nodes, "links": self.links}

        # set up correct file directory
        mypath = path.dirname(path.realpath(__file__))
        destination_file = (path.join(mypath, pardir) + "/data.json")

        with open(destination_file, 'w') as outfile:
            json.dump(data, outfile, indent=2, sort_keys=True)
