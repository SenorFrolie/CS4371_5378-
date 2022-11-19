from transaction import Transaction
from TangleGraph import TangleGraph

Graph = TangleGraph()

newtr = Transaction('234234', 'genesis', 25000000000)
Graph.AddTransaction(newtr)
newtr = Transaction('78273', 'genesis', 234234)
Graph.AddTransaction(newtr)

print(list(Graph.DAG))

for i in Graph.DAG:
    print(i)
    print(Graph.DAG[i].weight)
    print(Graph.DAG[i].source)
    print( Graph.DAG[i].destination)

    
