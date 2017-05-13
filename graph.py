def adjacency_matrix(file):
    ''' Parse adjacency list file into adjacency matrix '''

    # Open and read lines from file
    with open(file, 'r') as f:
        adj_list = f.readlines()

    # Initialize matrix
    n = len(adj_list)
    matrix = [[0 for i in range(n)] for j in range(n)]

    for i, vertex in enumerate(adj_list):
        # Extract edges in adjacency list
        edges = vertex.split()
        for edge in edges:
            try:
                j = int(vertex)
            except ValueError:
                continue
            # Insert edge into adjacency matrix
            matrix[i][j] = 1

    return matrix

def node_attributes(index):
    ''' get details of node in graph '''
    pass

def scc_network(matrix):
    ''' Check if network is strongly connected to confirm PageRank converges '''
    return False