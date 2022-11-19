from transaction import Transaction

# nodes will be able to issue transactions and validate others
class TangleNode:
    def __init__(self, transaction):
        self.id = None
        self.transaction = transaction
        #a field that keeps track of validated nodes

    # some functions that need to be implemented 
    # - selectTip
    # - validateTip