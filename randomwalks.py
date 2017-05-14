''' Perform random walks on graph ''' 
import random

def random_walk(adj_list, k, s=1):
    ''' Random walk of k steps on the graph.
        With probability s, walker chooses a random edge connected to current node.
        With probability 1-s, walker jumps to a random node anywhere in the graph.
    '''
    r = random.SystemRandom()
    current_node = -1
    for i in range(k):
        if current_node == -1 or r.random() < 1 - s:
            current_node = random.randrange(len(adj_list))
        else:
            if len(adj_list[current_node]) > 0:
                edge = random.randrange(len(adj_list[current_node]))
                current_node = adj_list[current_node][edge]
            else:
                current_node = current_node
    return current_node

def random_walks(adj_list, k, num_walks, s=1):
    ''' Perform a random walk on graph num_walks times 
        and keep track of frequencies
    '''
    frequencies = {}
    for i in range(num_walks):
        end_node = random_walk(adj_list, k, s)
        if end_node not in frequencies:
            frequencies[end_node] = 1
        else:
            frequencies[end_node] += 1
    
    return frequencies
        

