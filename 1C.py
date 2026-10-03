import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
G.add_edges_from([("A","B"),("B","C"),("D","E")])

print("Is A reachable from E ?",nx.has_path(G,"A","E"))
print("Is B reachable from C ?",nx.has_path(G,"B","C"))
print("Is D reachable from E ?",nx.has_path(G,"D","E"))
print("Is A reachable from C ?",nx.has_path(G,"A","C"))
print("Is D reachable from B ?",nx.has_path(G,"D","B"))

nx.draw(G,nx.spring_layout(G),with_labels=True,
        node_color="orange",node_size=2000)
plt.title("Graph with Less Reachability(Disconnected Components)")
plt.show()
