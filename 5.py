# Step 1: Import Libraries
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
print("Libraries imported successfully")


# Step 2: Create Dataset
emails = pd.DataFrame({
    "Sender": [
        "CEO","CEO","CEO","HR","HR","Finance","Finance","Manager","Manager","Manager",
        "Developer1","Developer2","Developer3","Research","Sales","Sales","Sales"
    ],
    "Receiver": [
        "HR","Finance","Manager","Manager","Developer1","CEO","Sales",
        "Developer1","Developer2","Research","Developer3","Developer3","Research",
        "CEO","CEO","Manager","Finance"
    ]
})

print("Email Dataset")
print(emails)


# Step 3: Edge List Representation
print("\n===== EDGE LIST =====")

for i, row in emails.iterrows():
    print(row["Sender"], "---->", row["Receiver"])


# Step 4: Create Graph
G = nx.from_pandas_edgelist(
    emails,
    source="Sender",
    target="Receiver",
    create_using=nx.DiGraph()
)

print("\n===== Graph Information =====")
print("Employees:")
print(list(G.nodes()))

print("\nConnections:")
print(list(G.edges()))


# Step 5: Adjacency Matrix
matrix = nx.to_pandas_adjacency(
    G,
    dtype=int
)

print("\n===== Adjacency Matrix =====")
print(matrix)


# Step 6: Adjacency Matrix HeatMap
import plotly.express as px
import plotly.io as pio

pio.renderers.default = "browser"

fig = px.imshow(
    matrix,
    text_auto=True,
    color_continuous_scale="Blues",
    labels={
        "x": "Receiver",
        "y": "Sender",
        "color": "Email Connection"
    },
    title="Interactive Corporate Email Adjacency Matrix"
)

fig.update_layout(
    width=800,
    height=700
)

fig.show()


# Step 7: Sociogram
import plotly.graph_objects as go

# Position of nodes
pos = nx.kamada_kawai_layout(G)

# Edges
edge_x = []
edge_y = []

for a, b in G.edges():
    x1, y1 = pos[a]
    x2, y2 = pos[b]

    edge_x += [x1, x2, None]
    edge_y += [y1, y2, None]

edges = go.Scatter(
    x=edge_x,
    y=edge_y,
    mode="lines",
    line=dict(color="gray", width=2),
    hoverinfo="none"
)


# Nodes
node_x = []
node_y = []
info = []

for n in G.nodes():
    x, y = pos[n]

    node_x.append(x)
    node_y.append(y)

    info.append(
        f"{n}<br>"
        f"Sent: {G.out_degree(n)}<br>"
        f"Received: {G.in_degree(n)}<br>"
    )

nodes = go.Scatter(
    x=node_x,
    y=node_y,
    mode="markers+text",
    text=list(G.nodes()),
    textposition="top center",
    hovertext=info,
    hoverinfo="text",
    marker=dict(
        size=35,
        color=node_x,
        colorscale="Viridis"
    )
)


fig = go.Figure([edges, nodes])

fig.update_layout(
    title="Corporate Email Network",
    showlegend=False,
    width=900,
    height=700,
    plot_bgcolor="lavender",
    xaxis_visible=False,
    yaxis_visible=False
)

fig.show()
