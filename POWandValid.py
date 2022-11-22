import hashlib
from transaction import *

# This document contains the calcPOW and validation functions that can be called
# when creating new transactions or checking the hashing of a tip for validation


# function to get pow for a transaction - returns a list of 2 elements
# at [0]:none [1]:pow hash
def calcPOW(transaction): 
    # This two elements will be used to get pow hash and nonce 
    nonce = 0
    hashData = str({
            'source': transaction.source,
            'destination': transaction.destination,
            'data': transaction.data 
        })
    # calculating the initial pow hash and nonce
    result = hashlib.sha256(hashData.encode() + str(nonce).encode())
    result = result.hexdigest()

    # while the pow hash does not meet the rule, increment nonce and rehash
    # This is basically solving the cryptographic puzzle to be able to join the
    # tangle, for now the rule is 2 zeros at the beginning
    while (result[0:2] != '00'):
        nonce +=1
        result = hashlib.sha256(hashData.encode() + str(nonce).encode())
        result = result.hexdigest()

    # return nonce and pow hash
    return [result, nonce]


# this functions checks if the original pow hash of a transaction is the same if
# if recalculated - used for tip validation, and avoid a transaction from 
# being validated if the data has been tampered
def validTipPOW(transaction):
        # get original hash
        originalHash = transaction.powHash

        # calculate hash with current data and nonce
        nonce = transaction.nonce
        hashData = str({
            'source': transaction.source,
            'destination': transaction.destination,
            'data': transaction.data 
        })
        currentHash = hashlib.sha256(hashData.encode() + str(nonce).encode())
        currentHash = currentHash.hexdigest()

        return (originalHash == currentHash)
