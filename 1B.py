import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
G.add_edges_from([
("Anand","Shashi"),
("Anand","Ajit"),
("Woldemort","Snape")
])

ego=nx.ego_graph(G,"Anand")

nx.draw(ego,with_labels=True,node_color="grey",node_size=3500)
plt.title("Ego Network of Anand")
plt.show()
