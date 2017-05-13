''' Run PageRank algorithm on the moon landing webgraph '''
import json
from graph import *
from pagerank import pagerank

f = open("data/newnodes.txt")
f.readlines()
f.read()



# Parse dataset into adjacency matrix
adj_list = adjacency_list("data/adj_list")
# Non scaled pagerank
rank = pagerank(adj_list, 10)

# output results
nodes = get_node_info("data/nodes")

# Append rank to nodes
for index, value in enumerate(rank):
    nodes[index]["pagerank"] = rank[index]

# Sort nodes by rank, desc
sorted_nodes = sorted(nodes, key=lambda k: k['pagerank'], reverse=True)

# Output ranking to file
with open('data/ranking.json', 'w') as f:
    json.dump(sorted_nodes, f)

