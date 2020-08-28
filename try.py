import networkx as nx
from louvain_modified import louvain_modified_algorithm
from community import community_louvain

structural_graph = nx.erdos_renyi_graph(500, 0.05)
N_edges = len(structural_graph.edges())
print('Number of edges in structural ER-graph: ', N_edges)

attributive_graph = nx.erdos_renyi_graph(500, 0.05)
N_edges = len(attributive_graph.edges())
print('Number of edges in attributive ER-graph: ', N_edges)

alpha = 1
partition = louvain_modified_algorithm.best_partition(structural_graph, attributive_graph, alpha=alpha)
Q1 = louvain_modified_algorithm.modularity(
    partition,
    structural_graph,
    attributive_graph,
    alpha=alpha)  # find modularity of the best partition
print(Q1) 

Q2 = community_louvain.modularity(partition, structural_graph) # check results if alpha = 0 or alpha = 1
print(Q2)

Q_structural = alpha * community_louvain.modularity(partition, structural_graph)  # find structural modularity contribution
print(Q_structural)

Q_attributive = alpha * community_louvain.modularity(partition, attributive_graph)  # find attributive modularity contribution
print(Q_attributive)
