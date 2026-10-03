import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edges_from([
    ("Alice","Bob"),("Alice","Charlie"),("Bob","Charlie"),
    ("Bob","David"),("Charlie","David"),("Charlie","Eva")
])

plt.figure(figsize=(8,6))
nx.draw(G, with_labels=True, node_color="lightblue",
        node_size=2000, edge_color="gray")
plt.title("Unipartite Sociogram")
plt.show()

B = nx.Graph()

people = ["Raiden","Kaiser","Sam","Ness","Leon","Wesker","Johan","Light"]
roles = ["Protagonist","Antagonist","Sides","Manipulators",
         "Soldier","Strategist","Slaves","Master"]

B.add_nodes_from(people, bipartite=0)
B.add_nodes_from(roles, bipartite=1)

B.add_edges_from([
    ("Raiden","Protagonist"),("Kaiser","Antagonist"),
    ("Ness","Sides"),("Sam","Antagonist"),
    ("Leon","Protagonist"),("Wesker","Antagonist"),
    ("Johan","Manipulators"),("Light","Protagonist"),
    ("Light","Manipulators"),("Johan","Antagonist"),
    ("Light","Strategist"),("Johan","Strategist"),
    ("Wesker","Strategist"),("Leon","Soldier"),
    ("Sam","Soldier"),("Kaiser","Master"),
    ("Ness","Slaves"),("Raiden","Soldier")
])

plt.figure(figsize=(14,14))
pos = nx.bipartite_layout(B, people)

nx.draw(B, pos, with_labels=True, node_size=3000,
        node_color=["lightblue" if n in people else "lightcoral"
                    for n in B.nodes()], font_size=10)

plt.title("Bipartite Sociogram")
plt.show()

C = nx.bipartite.projected_graph(B, people)

plt.figure(figsize=(8,6))
nx.draw(C, with_labels=True, node_color="lightblue",
        node_size=2000, edge_color="gray")
plt.title("Unipartite Projection")
plt.show()
