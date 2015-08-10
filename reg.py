import regex as re
import networkx as nx
import matplotlib.pyplot as plt

G=nx.DiGraph()

f = open('FinancialMaths.map', 'r')


# print (re.split(r'(s*)', 'here are some words'))
blob = f.read()
# blob = "MFIN094 -> MFIN092 -> MFIN100 -> MFIN101"
# print (re.findall(r'[A-z]{4}\d{3,4}', blob), re.I | re.M)

# print (re.findall(r'type="\w*"', blob), re.I | re.M)

blob2 = (re.findall(r"\{[^}]*", blob), re.MULTILINE)

# edge_dict = (re.findall(r'[A-z]{4}\d{3,4}\s*\[\w*type="\w*"\w*label="\w*"\w*]', blob, overlapped=True))
node_dict = (re.findall(r'[A-z]{4}\d{3,4}\s*\[.*type=\".*\".*label=\".*\".*]', blob, overlapped=True))


for node in node_dict:
    n = re.match(r'[A-z]{4}\d{3,4}', node)[0]
    G.add_node(n)

print G.number_of_nodes()
# print G.nodes()

extra_nodes = (re.findall(r'[A-z]{4}\d{3,4}\s?/\*.*\*/', blob), re.I | re.M)
for node in extra_nodes[0]:
    n = re.match(r'[A-z]{4}\d{3,4}', node)[0]
    # print node
    G.add_node(n)

print G.number_of_nodes()

edge_dict = (re.findall(r'[A-z]{4}\d{3,4}\s?->\s?[A-z]{4}\d{3,4}', blob, overlapped=True))

# print edge_dict

relationship_array = []

for pair in edge_dict:
    matches = re.findall(r'[A-z]{4}\d{3,4}', pair)
    tup = (matches[0], matches[1])
    relationship_array.append(tup)

# # # # EDGE CASE # # # #
edge_dict2 = (re.findall(r'[A-z]{3,4}\d{3,4}\s?/\*.*\*/\s?->\s?[A-z]{4}\d{3,4}', blob))

print "EDGE CASES"
for thing in edge_dict2:
    print thing


"STRIP IT"
for pair in edge_dict2:
    matches = re.findall(r'[A-z]{3,4}\d{3,4}', pair)
    print matches[0] + " -> " + matches[1]
    tup = (matches[0], matches[1])
    relationship_array.append(tup)

print "there are " + str(len(relationship_array)) + " edges"

for tup in relationship_array:
    # print tup[0] + " -> " + tup[1]
    G.add_edge(tup[0], tup[1])

# print (re.findall(r'[A-z]{4}\d{3,4}\s->\s[A-z]{4}\d{3,4}', blob), re.I | re.M)

# print edge_dict

print ('MFIN094 -> MFIN092' in edge_dict)

print ('MFIN092 -> MFIN100' in edge_dict)

print ('MFIN802->MFIN803' in edge_dict)

print ('MFIN802->MFIN807' in edge_dict)


nx.draw_random(G)
plt.savefig("random2.png")

# nx.draw_circular(G)
# plt.savefig("circular.png")

# nx.draw_spring(G)
# plt.savefig("spring.png")

# nx.draw_shell(G)
# plt.savefig("shell.png")

# nx.draw_graphviz(G)
# plt.savefig("graphviz.png")

# print word_dict[0][0]

f.close()
