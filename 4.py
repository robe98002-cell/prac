import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from([
    ("Alice","Bob"),("Bob","Charlie"),("Charlie","David"),
    ("David","Eva"),("Eva","Bob"),("Bob","Frank"),
    ("Alice","George"),("George","Hanah")
])

nx.draw(G, with_labels=True, node_color="skyblue",
        node_size=1500, edge_color="gray")
plt.title("Social Network Graph")
plt.show()

path = nx.shortest_path(G, "Alice", "Eva")
print("Shortest path From Alice To Eva:", path)

print("Network Density:", round(nx.density(G), 2))

ego = nx.ego_graph(G, "Bob")
nx.draw(ego, with_labels=True, node_color="orange",
        node_size=2000, edge_color="Black")
plt.title("Bob Ego Network")
plt.show()
