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
                j = int(edge)
            except ValueError:
                continue
            # Insert edge into adjacency matrix
            if j > 0:
                matrix[i][j] = 1

    return matrix

def adjacency_list(file):
    ''' Parse adjacency list file into adjacency list '''

    # Open and read lines from file
    with open(file, 'r') as f:
        adj_list_text = f.readlines()
    
    # Initialize list
    n = len(adj_list_text)
    adj_list = [[] for i in range(n)]

    for i, vertex in enumerate(adj_list_text):
        edges = vertex.split()
        for edge in edges:
            try:
                j = int(edge)
                if j > 0:
                    adj_list[i].append(j)
            except ValueError:
                continue
    return adj_list

def get_node_info(file):
    ''' Get list of dictionary objects. To get attributes of node n,
    node_info[n][key], where key = id, set, url, title, indegree, outdegree
    '''
    with open(file, 'r') as f:
        content = f.read()
    content = content.split("\n\n")
    content = content[1:]
    node_info = []
    for node in content:
        print(node)
        attributes = {}
        attributes['id'] = node.split("\n")[0].split()[0]
        attributes['set'] = node.split("\n")[0].split()[2]
        attributes['url'] = node.split("\n")[1]
        attributes['title'] = node.split("\n")[2]
        attributes['indegree'] = int(node.split("\n")[3].split()[0])
        attributes['outdegree'] = int(node.split("\n")[3].split()[1])
        node_info.append(attributes)
    return node_info
