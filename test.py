from transaction import *
from TangleGraph import *
import random as rn
from math import *
import matplotlib.pyplot as plt
import networkx as nx

# Just testing some of the functions and classes
# creating a test tangle graph and adding random trasactions
Graph = TangleGraph()

lamb = 10
id = 0

# Returning a number between 0-1


def random():
    return 0 + (100-50)*rn.random()


def genExp(lamb):
    x = 0
    while x == 0:
        u = rn.random()
        x = (-1/lamb)*log(u)
    return x


numberofTransaction = 0


while (numberofTransaction <= 3):
    # (self, id,source, destination, data, validated):
    tips = Graph.selectTips()
    newtr = Transaction(id, genExp(lamb), genExp(lamb), genExp(lamb), tips)
    Graph.AddTransaction(newtr)
    id += 1
    numberofTransaction += 1
# TODO: Display the cumulative Weight onto the graph

    CumulaWeight = newtr.GetCumulativeWeight()
    edges = Graph.edges
    nodes = []

    print("Weight here: ", newtr.GetCumulativeWeight())
    #print("Node: ", nodes, " Cumulative Weight: ", newtr.GetCumulativeWeight() )


    for i in edges.keys():
        for j in edges[i]:
             nodes.append(((i,Graph.DAG[i].cumulativeWeight),(j,Graph.DAG[j].cumulativeWeight)))

G = nx.DiGraph()            # creating an empty graph structure with no nodes and edges
G.add_edges_from(nodes)     # Adds the nodes with edges
nx.draw_networkx(G, arrows=True)
#plt.title("Tangle")
plt.show()


    
'''''
CumulaWeight = newtr.GetCumulativeWeight()

edges = Graph.edges
nodes = []
for i in edges.keys():
    for j in edges[i]:
        nodes.append((i,j))

G = nx.DiGraph()
G.add_edges_from(nodes, CumulaWeight = newtr.GetCumulativeWeight)
plt.tight_layout()
nx.draw(G, arrows=True)
plt.title("Tangle")
plt.show()
'''''


################
# tips = Graph.selectTips()
# newtr1 = Transaction('transac1', 'dfvsfbv', 'dfsvsfdv', 456456, tips)
# Graph.AddTransaction(newtr1)

# tips = Graph.selectTips()
# newtr2 = Transaction('transac2', '54545', '56515121', 456456, tips)
# Graph.AddTransaction(newtr2)

# tips = Graph.selectTips()
# newtr3 = Transaction('transac3', '848454', '5874156489', 15150215, tips)
# Graph.AddTransaction(newtr3)

# tips = Graph.selectTips()
# newtr4 = Transaction('transac4', '54545', '56515121', 952656065, tips)
# Graph.AddTransaction(newtr4)


# print in current transactions in DAG
for i in Graph.DAG:
    Graph.DAG[i].printDecryptedTransaction()
    Graph.DAG[i].printEncryptedTransaction()

# edges and opposite edges
# print('Edges')
# for i in Graph.edges:
#     print(i, Graph.edges[i])
# print('\n')

# print('Opposite Edges')
# for i in Graph.oppositeEdges:
#     print(i, Graph.oppositeEdges[i])
# print('\n')

# changing some data to check the valid fuction - should be false
# for i in Graph.DAG:
#     print(validTipPOW(Graph.DAG[i]))
