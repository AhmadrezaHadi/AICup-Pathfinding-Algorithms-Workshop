import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def graph(n):
    G = nx.grid_2d_graph(n, n)
    pos = {(x,y):(y,-x) for x,y in G.nodes()}
    for (u, v) in G.edges():
        G.edges[u,v]['weight'] = np.random.randint(1,31)
        # G.edges[u,v]['weight'] = 1
    return G, pos

def draw(G, pos):
    plt.figure(figsize=(7,7))
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw(G, pos=pos, 
            node_color='lightblue',
            with_labels=True,
            node_size=900,)
    nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=labels, rotate=False, font_color='green');


def draw_path(G, source, destination, path, pos):
    edge_list = [(i, path[idx+1]) for idx, i in enumerate(path) if idx < len(path)-1]
    draw(G, pos=pos)
    nx.draw_networkx_edges(G,pos=pos,edgelist=edge_list,edge_color = 'gray', width=10)
