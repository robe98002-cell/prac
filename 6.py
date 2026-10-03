import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
from itertools import combinations

G = nx.DiGraph()
G.add_edges_from([
    ("Alice","Manager"),("Bob","Manager"),("Charlie","Manager"),
    ("Manager","HR"),("Manager","Finance"),
    ("HR","CEO"),("Finance","CEO")
])

plt.figure(figsize=(8,6))
nx.draw(G, nx.spring_layout(G, seed=42), with_labels=True,
        node_color="orange", node_size=2000, arrows=True)
plt.title("Corporarate Communication Network")
plt.show()

def structural_equivalent(G):
    return [(u,v) for u,v in combinations(G.nodes(),2)
            if set(G.successors(u)) == set(G.successors(v))
            and set(G.predecessors(u)) == set(G.predecessors(v))]

print("Structurally Equivalent Pair:")
print(structural_equivalent(G))

def automorphically_equivalent(G):
    result = []
    for u,v in combinations(G.nodes(),2):
        mapping = {n: v if n == u else u if n == v else n for n in G}
        if nx.is_isomorphic(G, nx.relabel_nodes(G, mapping)):
            result.append((u,v))
    return result

print("Possible Automorphic Equivalence")
print("Alice,Bob and Charlie all have identical ties - can be swapped without breaking structure.")
print("Automorphically Equivalent Pairs:")
print(automorphically_equivalent(G))

roles = {}
for node in G:
    p, s = set(G.predecessors(node)), set(G.successors(node))
    if not p and s == {"Manager"}:
        roles[node] = "Employee"
    elif p == {"Alice","Bob","Charlie"}:
        roles[node] = "Manager"
    elif p == {"Manager"} and "CEO" in set(G.successors("HR")) | set(G.successors("Finance")):
        roles[node] = "Department"
    elif p == {"HR","Finance"}:
        roles[node] = "CEO"
    else:
        roles[node] = "Other"

role_df = pd.DataFrame.from_dict(roles, orient="index", columns=["Role"])
role_df
