from pyvis.network import Network
import pandas as pd

G = Network(height="750px", width="100%", directed=True)

# read the csv
data = pd.read_csv("BP_triple.csv")

edge_data = zip(data['node1'], data['node2'], data['relation'])

for e in edge_data:
    src, dst, edge = e[0], e[1], e[2]

    G.add_node(src, src, size=50, title=src, shape="box")
    G.add_node(dst, dst, size=50, title=dst, shape="box")
    G.add_edge(src, dst, title=edge)

G.show("schema.html")
print("File saved")
