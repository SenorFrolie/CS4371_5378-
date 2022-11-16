import time
class Transaction():
    def __init__(self, source, destination, data, *args):
        # transaction fields
        self.timeStamp = time.time()
        self.weight = 1
        self.cumulativeWeight = 0
        self.pow = None
        self.data = data
        self.source = source
        self.destination = destination
        # this will be used to get pow
        self.hashData = {
            'source': source,
            'destination': destination,
            'data': data 
        }

    #get proof of work
    def calcPOW(self):   
        return
