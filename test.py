from transaction import Transaction
from TangleGraph import TangleGraph

Graph = TangleGraph()

newtr = Transaction('234234', '[genesis]', 25000000000)

Graph.AddTransaction(newtr, Graph)

print(list(Graph.DAG))
