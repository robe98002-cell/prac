import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()

G.add_edges_from([
("Rohit","Dhoni"),("Rohit","Bumrah"),("Dhoni","Bumrah"),
("Dhoni","Ravi"),("Bumrah","Ravi"),("Ravi","Siraj"),
("Siraj","Gill"),("Gill","krish"),("krish","Rohit"),
("Virat","krish")
])

plt.figure(figsize=(8,6))
nx.draw(G,nx.spring_layout(G,seed=42),with_labels=True,
        node_color="lightgreen",node_size=1500,edge_color="black")
plt.title("Connected Social Network Graph")
plt.show()

print(f"Graph is fully recheable(connected):{nx.is_connected(G)}")
print(f"Number of connected components:{nx.number_connected_components(G)}")
print(f"Network Density:{nx.density(G):.2f}")

print("\nAdjacency List:")
for node in G.adj:
    print(f"{node}:{list(G.adj[node])}")
