import time
import hashlib

# function to get pow for the new transaction
# still needs a rule for proof of work and check the validity of it
def calcPOW(data):  
    data = str(data)
    result = hashlib.sha256(data.encode())
    return result.hexdigest()

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

        # this will be used to get pow
        self.hashData = {
            'source': source,
            'destination': destination,
            'data': data 
        }
        # calculate proof of work
        self.pow = calcPOW(self.hashData)
        return

    #print trasaction information - mainly for testing
    def printTransaction(self):
        print("ID: ",self.id)
        print("Cumulative Weight: ", self.cumulativeWeight)
        print("Time: ", self.timeStamp)
        print("Destination: ", self.destination)
        print("Source: ", self.source)
        print("Data: ", self.data)
        print("POW: ", self.pow)
        print('\n')