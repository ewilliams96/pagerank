''' Pagerank '''

def init_rank_vector(n):
    ''' Initialize rank vector of size n, with each node assigned initial rank 1/n
        Return new rank vector
    '''
    return [1/n for i in range(n)]

def pagerank_scale(rank_vector, s):
    residual = 1 - s
    equal_share = residual / len(rank_vector)
    # Scale down by s
    rank_vector[:] = [x * s for x in rank_vector]
    # Redistribute residual equally 
    rank_vector[:] = [x + equal_share for x in rank_vector]

def pagerank_update(adj_list, rank_vector, scaled, s):
    ''' Perform pagerank update step and update values of matrix and rank_vector
        Return True if equilibrium is hit 
    '''
    # Copy old rank vector to calculate new values
    old_rank = list(rank_vector)

    # Clear current rank vector
    for i in range(len(rank_vector)):
        rank_vector[i] = 0

    # Each page divides its current pagerank equally across its outgoing links
    for index, edges in enumerate(adj_list):
        # If no outgoing links: pass current pagerank to itself
        if len(edges) == 0:
            rank_vector[index] += old_rank[index]
            continue
        # Add equal share of its pagerank to each outgoing link
        equal_share = old_rank[index] / len(edges)
        for edge in edges:
            rank_vector[edge] += equal_share
    
    # Perform scaling if scaled = True:
    if scaled:
        pagerank_scale(rank_vector, s)

    # Return True if equillibrium: ranks did not change
    if old_rank == rank_vector:
        return True
    else:
        return False


def pagerank(adj_list, k, scaled=False, s=0.85):
    ''' Perform PageRank algorithm on provided adjacency list with k steps, 
        or until equillibrium values are reached.

        adj_list -- graph to perform PageRank algorithm on
        k -- number of steps of PageRank
        scaled -- False to perform basic PageRank, True to perform scaled PageRank. Default: False
        s -- Scaling factor. If not provided, use 0.85
        Return final rank vector
    '''

    rank_vector = init_rank_vector(len(adj_list))

    for i in range(k):
        ret = pagerank_update(adj_list, rank_vector, scaled, s)

    return rank_vector

