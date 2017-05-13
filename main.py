''' Run PageRank algorithm on the moon landing webgraph '''
from graph import adjacency_matrix
from pagerank import pagerank

# Parse dataset into adjacency matrix
matrix = adjacency_matrix("data/adj_list")
# Non scaled pagerank
pagerank(matrix, 10)