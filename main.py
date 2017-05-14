''' Run PageRank algorithm on the moon landing webgraph '''
from graph import adjacency_list
from pagerank import pagerank
from results import output_rank_json, output_rank_csv, output_random_walks
from randomwalks import random_walks

# Parse dataset into adjacency matrix
adj_list = adjacency_list("data/adj_list")
# Non scaled pagerank
rank = pagerank(adj_list, 10)

# output results of basic pagerank
output_rank_json("data/nodes", rank, "out/unscaledranking.json")
output_rank_csv("data/nodes", rank, "out/unscaledranking.csv")


# Scaled pagerank s = 0.85
scaled_rank = pagerank(adj_list, 10, scaled=True)

# output results of scaled pagerank
output_rank_json("data/nodes", scaled_rank, "out/scaledranking.json")
output_rank_csv("data/nodes", scaled_rank, "out/scaledranking.csv")

# Scaled pagerank s = 0.7
scaled_rank = pagerank(adj_list, 10, scaled=True, s=0.7)
output_rank_csv("data/nodes", scaled_rank, "out/scaledranking7.csv")

# Scaled pagerank s = 0.5
scaled_rank = pagerank(adj_list, 10, scaled=True, s=0.5)
output_rank_csv("data/nodes", scaled_rank, "out/scaledranking5.csv")

# Scaled pagerank s = 0.3
scaled_rank = pagerank(adj_list, 10, scaled=True, s=0.3)
output_rank_csv("data/nodes", scaled_rank, "out/scaledranking3.csv")

# Scaled pagerank s = 0.1
output_rank_csv("data/nodes", scaled_rank, "out/scaledranking1.csv")
scaled_rank = pagerank(adj_list, 10, scaled=True, s=0.1)

# Random walks

# Unscaled random walk s = 1
frequencies = random_walks(adj_list, 10, 500000, 1)
output_random_walks("data/nodes", frequencies, "out/randomwalkunscaled.csv")


# Scaled random walk s = .85
frequencies = random_walks(adj_list, 10, 500000, 0.85)
output_random_walks("data/nodes", frequencies, "out/randomwalkscaled.csv")


