#!/usr/bin/env python3
from sys import argv
import networkx as nx

G = nx.Graph()
filename = argv[1]
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        edge = line.split(')')
        G.add_edge(*edge)
print('Part 1:', sum(nx.algorithms.shortest_path_length(G, 'COM').values()))
