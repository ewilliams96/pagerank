''' Pagerank '''

def init_rank_vector(n):
    ''' Initialize rank vector of size n, with each node assigned initial rank 1/n
        Return new rank vector
    '''
    return None

def pagerank_update(matrix, rank_vector):
    ''' Perform pagerank update step and update values of matrix and rank_vector
        Return True if equillibrium is hit 
    '''
    
    # Each page divides its current PageRank equally accross outgoing links

    # Each page updates its new pagerank to be the sum of the shares it receives
    return False

def pagerank(matrix, k):
    ''' Perform basic PageRank algorithm on provided adjacency matrix with k steps, 
        or until equillibrium values are reached.
        Return final rank vector
    '''
    return None