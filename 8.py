import networkx as nx
import matplotlib.pyplot as plt

coordinator = "Fest Coordinator"
leads = ["Publicity","PR","Event","Admin","Hospitality","Tech n logs"]

volunteers = {
    "Publicity":["vinayak","parth"],
    "PR":["onkar","karan"],
    "Event":["tanvi","surya"],
    "Admin":["atharva"],
    "Hospitality":["krishna","ayushi"],
    "Tech n logs":["Divya","Ravi"]
}

B = nx.Graph()
B.add_node(coordinator, bipartite=0, role="Coordinator")
B.add_nodes_from(leads, bipartite=0, role="Lead")

for lead, vols in volunteers.items():
    B.add_nodes_from(vols, bipartite=1, role="Volunteer")
    B.add_edges_from((lead, vol) for vol in vols)

B.add_edges_from((coordinator, lead) for lead in leads)

# Two-mode network
top = [n for n,d in B.nodes(data=True) if d["bipartite"] == 0]
bottom = [n for n,d in B.nodes(data=True) if d["bipartite"] == 1]

pos = {n:(i,1) for i,n in enumerate(top)}
pos.update({n:(i,0) for i,n in enumerate(bottom)})

colors = [
    "lightblue" if d["role"]=="Coordinator"
    else "orange" if d["role"]=="Lead"
    else "pink"
    for _,d in B.nodes(data=True)
]

plt.figure(figsize=(12,6))
nx.draw(B, pos, with_labels=True, node_color=colors,
        node_size=3500, font_weight="bold")
plt.title("Two-mode Network: Fest Coordinator, Leads,Volunteers")
plt.show()

# One-mode projection
P = nx.bipartite.projected_graph(B, leads)

plt.figure(figsize=(8,6))
nx.draw(P, with_labels=True, node_color="lightblue",
        node_size=2000, font_weight="bold")
plt.title("One-mode projection: Lead-to-lead network (Shared volunteers)")
plt.show()

