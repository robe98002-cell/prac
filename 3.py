import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from([
    ('A','B'),('A','C'),('B','C'),
    ('B','D'),('C','D'),('C','E')
])

plt.figure(figsize=(6,4))
nx.draw(G, with_labels=True, node_color='lightblue',
        node_size=1500, font_size=14)
plt.title('simple graph')
plt.show()

d = nx.degree_centrality(G)
print("Degree Centrality:")
for n,c in d.items():
    print(f"Node {n}: {c:.2f}")

b = nx.betweenness_centrality(G)
print("\nBetweeness Centrailty:")
for n,c in b.items():
    print(f":Node{n}: {c:.2f}")

c = nx.closeness_centrality(G)
print("\nCloseness Centrality:")
for n,x in c.items():
    print(f"Node {n}:{x:.2f}")

e = nx.eccentricity(G)
m = min(e.values())
centers = [n for n,x in e.items() if x == m]

print("\nEccentricity of Nodes.")
for n,x in e.items():
    print(f"Node {n}: {x}")
print(f"\nGraph Centers (min eccentricity ={m}): {centers}")

DG = G.to_directed()
print(f"\nReciprocity of the directed graph: {nx.reciprocity(DG):.2f}")

cl = nx.clustering(G)
print("\nClustering Coefficient:")
for n,x in cl.items():
    print(f"Node {n}: {x:.2f}")
