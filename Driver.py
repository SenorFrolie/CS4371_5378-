from transaction import *
from TangleGraph import * 
import random as rn
from math import *
import matplotlib.pyplot as plt
import networkx as nx

# amount of nodes that will be added to the Tangle - can be changed by user
AMOUNT = int(input ("Enter number of transaction to be generated: "))

#Functions to generate random data for transanctions
lamb = 10
# Returning a number between 0-1
def random():
    return 0 + (100-50)*rn.random()
def genExp(lamb):
    x = 0
    while x == 0:
        u = rn.random()
        x = (-1/lamb)*log(u)
    return x

# creating a test tangle graph and adding random trasactions
Graph = TangleGraph()
numberofTransaction = 0
id = 0
while(numberofTransaction <= AMOUNT):
    #(self, id,source, destination, data, validated):   
    tips = Graph.selectTips()
    newtr = Transaction(id, genExp(lamb), genExp(lamb),genExp(lamb), tips)
    Graph.AddTransaction(newtr)
    id+=1
    numberofTransaction +=1

# print in current transactions in DAG 
for i in Graph.DAG:
    Graph.DAG[i].printDecryptedTransaction()
    Graph.DAG[i].printEncryptedTransaction()

# Visualization for tangle Graph
edges = Graph.edges
nodes = []
nodes_color = []
for i in edges.keys():
    for j in edges[i]:
        if i == None:
            continue
        if j == None:
            continue
        nodes.append(((i,Graph.DAG[i].cumulativeWeight),(j,Graph.DAG[j].cumulativeWeight)))

# get different colors for tips and validated nodes
for i in Graph.DAG:
    if Graph.DAG[i].cumulativeWeight <= 1:
        nodes_color.append("red")
    else:
        nodes_color.append("cyan")

G = nx.DiGraph()
G.add_edges_from(nodes)
plt.tight_layout()
nx.draw_networkx(G, arrows=True, node_color=nodes_color, node_size=1000, font_weight='bold', pos=nx.spring_layout(G,k=4))
plt.title("Tangle")
plt.show()