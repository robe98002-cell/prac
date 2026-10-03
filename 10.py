import networkx as nx
import matplotlib.pyplot as plt
# Create a bipartite graph
B = nx.Graph()
# Define two sets of nodes
actors = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
movies = ['M1', 'M2', 'M3', 'M4']
# Add nodes with a 'bipartite' attribute
B.add_nodes_from(actors, bipartite=0) # Top set
B.add_nodes_from(movies, bipartite=1) # Bottom set
edges = [
("Alice", "M1"), ("Bob", "M1"), ("Charlie", "M1"),
("Alice", "M2"), ("David", "M2"),
("Eva", "M3"),
("Bob", "M4"), ("Charlie", "M4"), ("Eva", "M4")
]
B.add_edges_from(edges)
from networkx.algorithms import bipartite
pos = nx.spring_layout(B)
nx.draw(
B,
pos,
with_labels=True,
node_color='skyblue',
edge_color='gray'
)
plt.title("Two Mode Network: Actor & Movies")
plt.show()

actor_graph = bipartite.projected_graph(B,actors)
nx.draw(actor_graph, with_labels=True,node_color='blue')
plt.title("Actor Co-Participation Network")
plt.show()
