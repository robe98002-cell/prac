import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from IPython.display import display,clear_output
import ipywidgets as widgets

df=pd.DataFrame({
"User1":["Alice","Alice","Alice","Bob","Bob","Charlie",
         "David","Eva","Frank","Grace","Harry","David"],
"User2":["Bob","Charlie","David","Charlie","Eva","Frank",
         "Eva","Frank","Grace","Harry","Alice","Grace"]
})

display(df)

G=nx.from_pandas_edgelist(df,"User1","User2")

degrees=dict(G.degree())

print("="*60)
print("Social Media Friendship Network Dashboard")
print("="*60)
print(f"Total Users :{G.number_of_nodes()}")
print(f"Total Friendships :{G.number_of_edges()}")
print(f"Most Connected User :{max(degrees,key=degrees.get)}")
print(f"Lowest Degree User :{min(degrees,key=degrees.get)}")

degree_df=pd.DataFrame(
    list(degrees.items()),
    columns=["User","Degree"]
).sort_values(by="Degree",ascending=False)

plt.figure(figsize=(8,5))
plt.bar(degree_df["User"],degree_df["Degree"],color="purple")
plt.title("Digital Distribution")
plt.xlabel("Users")
plt.ylabel("Degree")
plt.grid(axis="y")
plt.show()

user_dropdown=widgets.Dropdown(
    options=list(G.nodes()),description="User:"
)

output=widgets.Output()

def update(change):
    with output:
        clear_output(wait=True)
        user=user_dropdown.value

        print(f"Selected User: {user}")
        print("Friends:",list(G.neighbors(user)))
        print("Degree:",G.degree(user))

        plt.figure(figsize=(6,4))
        pos=nx.spring_layout(G,seed=42)

        nx.draw_networkx(
            G,pos,
            node_color=[
                "purple" if n==user else "purple"
                for n in G.nodes()
            ],
            node_size=2500
        )

        plt.show()

user_dropdown.observe(update,names="value")
display(user_dropdown,output)
update(None)
