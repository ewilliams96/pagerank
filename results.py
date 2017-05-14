''' Helpers for outputting results '''

import json
import csv
from graph import get_node_info

def output_rank_json(node_file, rank, outfile):
    ''' Attatch pagerank results to nodes and write to JSON'''
    nodes = get_node_info(node_file)

    # Append rank to nodes
    for index, value in enumerate(rank):
        nodes[index]["pagerank"] = rank[index]

    # Sort nodes by rank, desc
    sorted_nodes = sorted(nodes, key=lambda k: k['pagerank'], reverse=True)

    # Output ranking to file
    with open(outfile, 'w') as f:
        json.dump(sorted_nodes, f)

def output_rank_csv(node_file, rank, outfile):
    ''' Attatch pagerank results to nodes and write to JSON'''
    nodes = get_node_info(node_file)

    # Append rank to nodes
    for index, value in enumerate(rank):
        nodes[index]["pagerank"] = rank[index]

    # Sort nodes by rank, desc
    sorted_nodes = sorted(nodes, key=lambda k: k['pagerank'], reverse=True)

    with open(outfile, 'w') as f:
        fields = ['title', 'url', 'set', 'indegree', 'outdegree', 'pagerank']
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for item in sorted_nodes:
            del item['id']
            writer.writerow(item)

def output_random_walks(node_file, frequencies, outfile):
    nodes = get_node_info(node_file)
    for index, node in enumerate(nodes):
        if index in frequencies:
            node["frequency"] = frequencies[index]
        else:
            node["frequency"] = 0
    sorted_nodes = sorted(nodes, key=lambda k: k['frequency'], reverse=True)

    with open(outfile, 'w') as f:
        fields = ['title', 'url', 'set', 'indegree', 'outdegree', 'frequency']
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for item in sorted_nodes:
            del item['id']
            writer.writerow(item)
