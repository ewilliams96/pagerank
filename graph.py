def adjacency_matrix(file):
    ''' get adjacency matrix from file '''

    # Open and read lines from file
    with open(file, 'r') as f:
        adj_list = f.readlines()

    # Initialize matrix
    n = len(adj_list)
    matrix = [[0 for i in range(n)] for j in range(n)]

    for index, line in enumerate(adj_list):
        #print(line)
        pass

    return matrix

def node_attributes(index):
    ''' get details of node in graph '''
    pass

def scc_network(matrix):
    ''' Check if network is strongly connected to confirm PageRank converges '''
    return False