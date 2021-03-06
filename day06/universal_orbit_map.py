#!/usr/bin/env python3
from sys import argv
import networkx as nx

G = nx.Graph()
filename = argv[1]
with open(filename) as f:
    for line in f:
        G.add_edge(*line.rstrip().split(')'))
print('Part 1:', sum(nx.algorithms.shortest_path_length(G, 'COM').values()))
print('Part 2:', len(nx.algorithms.shortest_path(G, 'YOU', 'SAN'))-3)
