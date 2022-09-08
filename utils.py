import networkx as nx
import numpy as np
import string
import matplotlib.pyplot as plt

def graph(source, destination):
    G = nx.grid_2d_graph(7, 7)
    mapping = {}
    pos = {}
    color= []
    i, j = 1, 1
    for idx, n in enumerate(G.nodes):
        name = string.ascii_letters[idx]
        mapping[n] = name
        pos[name] = (i, j)
        if name == source:
            color.append('lightgreen')
        elif name == destination:
            color.append('red')
        else:
            color.append('lightblue')
        if i%7==0:
            i=0
            j+=1
        i+=1
        
    G = nx.relabel_nodes(G, mapping=mapping)    
        
        
    for (u, v) in G.edges():
        G.edges[u,v]['weight'] = np.random.randint(1,15)

    return G, pos, color


def draw_path(G, pos, path, color):
    plt.figure(figsize=(6,5))
    edge_list = [(i, path[idx+1]) for idx, i in enumerate(path) if idx < len(path)-1]
    # pos = nx.spring_layout(G)
    # nx.draw_networkx_nodes(G,pos=pos)
    # nx.draw_networkx_labels(G,pos=pos)
    nx.draw(G, pos=pos, 
        node_color=color, 
        with_labels=True,
        node_size=600)
    colors = ['r', 'b', 'y']
    linewidths = [20,10,5]
    nx.draw_networkx_edges(G,pos=pos,edgelist=edge_list,edge_color = 'gray', width=10)
