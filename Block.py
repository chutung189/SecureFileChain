import hashlib

class Block:
    #Each block will include its index, all transactions, and its previous hash
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index  # index of each block
        self.timestamp = timestamp
        self.data = data  # dict chứa thông tin file
        self.previous_hash = previous_hash # hash of the previous block. 
        self.nonce = 0 # nonce useful for mining new block using POW consensus
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        data_string = str(self.index) + str(self.timestamp) + str(self.data) + self.previous_hash + str(self.nonce)
        return hashlib.sha256(data_string.encode()).hexdigest()

    # creates a hash for the block
    def generate_hash(self):
        #  generates hash code using the values stored in block instance. completely random  
        all_data_combined = str(self.index) + str(self.nonce) + self.previous_hash + str(self.data)
        return hashlib.sha256(all_data_combined.encode()).hexdigest()