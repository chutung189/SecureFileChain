import hashlib
from hashlib import sha256
#multiple blocks linked together will make a blockchain
class Block:
    #Each block will include its index, all transactions, and its previous hash
    def __init__(self, index, timestamp, transactions, prev_hash):
        self.index = index  # index of each block
        self.timestamp = timestamp
        self.transactions = transactions # transactions (information about files stored in a block)
        self.prev_hash = prev_hash # hash of the previous block. 
        self.nonce = 0 # nonce useful for mining new block using POW consensus
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        data_string = str(self.data) + self.previous_hash + str(self.timestamp) + str(self.nonce)
        return hashlib.sha256(data_string.encode()).hexdigest()

    # creates a hash for the block
    def generate_hash(self):
        #  generates hash code using the values stored in block instance. completely random  
        all_data_combined = str(self.index) + str(self.nonce) + self.prev_hash + str(self.transactions)
        return sha256(all_data_combined.encode()).hexdigest()
    
    def add_t(self, t):
        self.transactions.append(t)