from transaction import *
from POWandValid import *
import random

# the graph will have nodes, which have transactions
class TangleGraph():
    # constructor for tangle graph
    # the graph is made up of a map containing the transaction objects, a map for edges
    # and a map for opposite edges
    def __init__(self):    
        GenesisID = 'genesis' #id for the genesis node, maybe we can use a random id generator like the uuid library

        # Make genesis node
        # source, destination, and data can be randomly generated, this are just initial values - maybe we can use the uuid libray
        GenesisIDTransaction = Transaction(GenesisID, 'GenesisSRC', 'GenesisDEST', '000000000' , None) 

        # add genesis node to DAG
        # DAG is a map that will contain the actual transactions
        # <id of transaction: Transaction object>
        self.DAG = {GenesisID: GenesisIDTransaction}

        # add genesis node to edges
        # a map containing the edges of the dag, basically an adjacency list, where
        # the key is the id of a transaction and the value is a list of ids of transactions
        # validated by that transaction.
        # <id of a transaction: [ids of transactions validated by the transaction in key]>
        self.edges = {GenesisID:[] } 

        # add genesis node to opposite edges
        # a map containing the opposite edges of the dag, similar to the edges map, but
        # keeping track of transactions that have validated a specific transaction,
        # can be useful for tip selection to make sure there is no cycles.
        # <id of a transaction: [ids of transactions that have validated the transaction in key]
        self.oppositeEdges = {GenesisID:[] } 


    # function that will select the tips for the new transaction to validate
    # It will select the most 2 recently added tips, and if those are invalid, it 
    # will choose two random tips
    def selectTips(self):
        # choose two random tips
        tip1 = random.choice(list(self.DAG))
        tip2 = random.choice(list(self.DAG))

        # if the genesis is the only transaction present return the genesis as the
        # selected tips
        if len(self.DAG) == 1:
            return [tip1,tip2]

        # choose the 2 most recently added tips
        tip1, tip2 = set(list(self.DAG.keys())[-2:])

        # if there is more than just the genesis node, choose different transactions
        # checking that the selected tip has a valid pow hash
        while not validTipPOW(self.DAG[tip1]):
            tip1 = random.choice(list(self.DAG))

        while  not (validTipPOW(self.DAG[tip2])) or tip1 == tip2:
            tip2 = random.choice(list(self.DAG))

        return [tip1,tip2]
    
    # function for calculating cummulative weight everytime a transaction is validated
    def changeCumulativeWeight(self, transaction):
        #print("top of CCW, transaction ID: ",transaction.id)

        # get weights of children 
        childWeights = 0 
        #print("self.oppositeEdges[{id}]]: {res}".format(id=transaction.id, res=self.oppositeEdges[transaction.id]))
        #print("self.edges[{id}]]: {res}".format(id=transaction.id, res=self.edges[transaction.id]))
        for children in self.oppositeEdges[transaction.id]:
            childWeights += self.DAG[children].cumulativeWeight
            #print("updated childWeights; new value: ",childWeights)
            
        # add weight to transaction cumulative weight
            transaction.cumulativeWeight = transaction.directWeight + childWeights
        # return once we hit genesis
        if transaction.id == 'genesis':
            #print("hit genesis node - returning now")
            return
        
        else: # update cumulative weight of parent node
            #print("self.edges[{id}]]: {res}".format(id=transaction.id, res=self.edges[transaction.id]))
            #print("self.edges[{id}][1]]: {res}".format(id=transaction.id, res=self.edges[transaction.id][1]))
            for parent in self.edges[transaction.id]:
                parentNode = self.DAG[parent]
                self.changeCumulativeWeight(parentNode)
            
                
    # function to add transactions to tangle graph, for now it's just adding the new transactions -
    # still needs validation of tips
    def AddTransaction(self, transaction):
        # add trasanction to DAG
        self.DAG[transaction.id] = transaction
        # make a list in opppositeEdges for new transaction - will empty for now, 
        # once another transaction validates this one, it will be added here
        self.oppositeEdges[transaction.id] = []

        # get the tips validated by transaction
        validatedTips = transaction.validated

        # check that transaction is not in edges yet, and add it along with the
        # two tips that it validated
        # <id of new transaction: [ids of transactions validated by this new transaction]>
        if transaction.id not in self.edges:
            self.edges[transaction.id] = validatedTips

        # check the opposite edges and add the new transaction to the adjacency list
        # of opposite edges of each approved transaction 
        # <id of approved transaction 1: [id of the new transaction being added]
        if validatedTips[0] not in self.oppositeEdges:
            self.oppositeEdges[validatedTips[0]] = [transaction.id]
        else:
            self.oppositeEdges[validatedTips[0]].append(transaction.id)
        # <id of approved transaction 1: [id of the new transaction being added]
        if validatedTips[1] not in self.oppositeEdges:
            self.oppositeEdges[validatedTips[1]] = [transaction.id]
        else:
            self.oppositeEdges[validatedTips[1]].append(transaction.id) 
            
        # recursively update cumulative weights until we hit the genesis node
        self.changeCumulativeWeight(transaction)
        