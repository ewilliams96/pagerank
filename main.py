''' Run PageRank algorithm on the moon landing webgraph '''
from graph import adjacency_list
from pagerank import pagerank
from results import output_rank_json, output_rank_csv

# Parse dataset into adjacency matrix
adj_list = adjacency_list("data/adj_list")
# Non scaled pagerank
rank = pagerank(adj_list, 10)

# output results of basic pagerank
output_rank_json("data/nodes", rank, "data/unscaledranking.json")
output_rank_csv("data/nodes", rank, "data/unscaledranking.csv")


# Scaled pagerank
scaled_rank = pagerank(adj_list, 10, scaled=True)

# output results of scaled pagerank
output_rank_json("data/nodes", scaled_rank, "data/scaledranking.json")
output_rank_csv("data/nodes", scaled_rank, "data/scaledranking.csv")


# Random walks
