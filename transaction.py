import time
# import hashlib
from POWandValid import *

class Transaction():
    def __init__(self, id,source, destination, data, validated):
        # transaction fields 
        self.id = id
        self.timeStamp = time.time()
        self.weight = 1
        self.cumulativeWeight = 0
        self.data = data
        self.source = source
        self.destination = destination
        # this field will keep the ids of transactions that were validated by
        # this transaction - the validated parameter will be the two selected tips
        # from the selectTips function
        self.validated = validated

        # calculate proof of work
        pow = calcPOW(self)
        self.powHash = pow[0]
        self.nonce = pow[1]

    #print trasaction information - mainly for testing
    def printTransaction(self):
        print("ID: ",self.id)
        print("Cumulative Weight: ", self.cumulativeWeight)
        print("Time: ", self.timeStamp)
        print("Destination: ", self.destination)
        print("Source: ", self.source)
        print("Data: ", self.data)
        print("POW: ", self.powHash)
        print("Nonce: ", self.nonce)
        print('\n')