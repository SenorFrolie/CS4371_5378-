import time
# import hashlib
from POWandValid import *
from Encryption import *

class Transaction():
    def __init__(self, id,source, destination, data, validated):
        # transaction fields 
        self.id = id
        self.timeStamp = time.time()
        self.weight = 1
        self.cumulativeWeight = self.weight
        self.data = Encrypt(data)
        self.source = Encrypt(source)
        self.destination = Encrypt(destination)
        # this field will keep the ids of transactions that were validated by
        # this transaction - the validated parameter will be the two selected tips
        # from the selectTips function
        self.validated = validated

        # calculate proof of work
        pow = calcPOW(self)
        self.powHash = pow[0]
        self.nonce = pow[1]

    #prints encrypted trasaction information
    def printEncryptedTransaction(self):
        print("ID: ",self.id)
        print("Cumulative Weight: ", self.cumulativeWeight)
        print("Time: ", self.timeStamp)
        print("Destination: ", self.destination)
        print("Source: ", self.source)
        print("Data: ", self.data)
        print("POW: ", self.powHash)
        print("Nonce: ", self.nonce)
        print('\n')

    #prints decrypted trasaction information
    def printDecryptedTransaction(self):
        print("ID: ",self.id)
        print("Cumulative Weight: ", self.cumulativeWeight)
        print("Time: ", self.timeStamp)
        print("Destination: ", Decrypt(self.destination))
        print("Source: ", Decrypt(self.source))
        print("Data: ", Decrypt(self.data))
        print("POW: ", self.powHash)
        print("Nonce: ", self.nonce)
        print('\n')