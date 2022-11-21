from transaction import *
from TangleGraph import *
from TangleGraph import *
 

# Just testing some of the functions and classes
# creating a test tangle graph and adding random trasactions
Graph = TangleGraph()

tips = Graph.selecTips()
newtr = Transaction('transac1', '4545645646', '4544454',456456456, tips)
Graph.AddTransaction(newtr)

tips = Graph.selecTips()
newtr2 = Transaction('transac2', '54545', '56515121', 456456, tips)
Graph.AddTransaction(newtr2)

tips = Graph.selecTips()
newtr3 = Transaction('transac3', '848454', '5874156489', 15150215, tips)
Graph.AddTransaction(newtr3)

tips = Graph.selecTips()
newtr4 = Transaction('transac4', '54545', '56515121', 952656065, tips)
Graph.AddTransaction(newtr4)

# print in current transactions in DAG 
for i in Graph.DAG:
    Graph.DAG[i].printTransaction()

# edges and opposite edges 
print('Edges')
for i in Graph.edges:
    print(i, Graph.edges[i])
print('\n')

print('Opposite Edges')
for i in Graph.oppositeEdges:
    print(i, Graph.oppositeEdges[i])
print('\n')
