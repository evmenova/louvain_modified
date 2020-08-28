import networkx as nx
from louvain_modified import louvain_modified_algorithm
from community import community_louvain

structural_graph = nx.erdos_renyi_graph(500, 0.05)
N_edges = len(structural_graph.edges())
print('Number of edges in structural ER-graph: ', N_edges)

attributive_graph = nx.erdos_renyi_graph(500, 0.05)
N_edges = len(attributive_graph.edges())
print('Number of edges in attributive ER-graph: ', N_edges)

Q1 = louvain_modified_algorithm.modularity(
    louvain_modified_algorithm.best_partition(structural_graph, attributive_graph, alpha=1),
    structural_graph,
    attributive_graph,
    alpha=1)
print(Q1)

Q2 = community_louvain.modularity(community_louvain.best_partition(structural_graph),
                                  structural_graph)
print(Q2)