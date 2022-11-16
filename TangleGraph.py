from transaction import Transaction

class TangleGraph(object):
    def __init__(self, *args):
        # making a list
        self.DAG = {}     
        # genesis node
        genesis_transaction = Transaction('0000', 'genesis', 456903404)        
        self.AddTransaction(genesis_transaction)

    # function to add transactions to dag - needs stuff like verification..
    def AddTransaction(self, transaction):
            self.DAG[transaction.source] = transaction
    
    # some functions that need to be implemented 
    # - selectTip
    # - validateTip

    