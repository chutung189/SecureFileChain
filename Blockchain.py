#Import libraries
import random
from Block import Block

#immutable list of blocks
class Blockchain:
    # Difficult for proof of work
    difficulty = 3
    #intialize our chain
    def __init__(self):
        self.chain = [] # blockchain
        genesis_data = {"filename": "Genesis", "CID": "", "file_hash": ""}
        genesis_block = Block(0, "2025-01-01 00:00:00", genesis_data, "0") #create a new intital block 
        genesis_block.hash = genesis_block.generate_hash() #generate hash for that block
        self.chain.append(genesis_block) #append it to our chain

    
    # Add a block to the chain after verfying and validating it. Input : block and hash of that block
    def add_block(self, block):
        prev_hash = self.last_block().hash
        #check the validity of the block
        if prev_hash == block.previous_hash and self.is_valid(block, block.hash):
            self.chain.append(block)
            return True
        else:
            return False


    # will add the block to the chain. This method is wrapper for verifying, validating and adding the block. Will take all pending transactions and create and append the blocks to our chain
    def mine(self, data):
        last_block = self.last_block() #get last block
        # Creates a new block to be added to the chain
        new_block = Block(
            index=last_block.index + 1,
            timestamp="2025-10-04 00:00:00",
            data=data,
            previous_hash=last_block.hash
        )

        # runs the our proof of work and gets the consensus. There are 2 different types of p_o_w implemented below. Replace the method name to try another one(p_o_w_2(new_block))
        new_block.hash = self.p_o_w(new_block)
        #add the block
        self.add_block(new_block)
        # Returns the index of the blockthat was added to the chain
        return new_block.index

    #generates a proof of work with the stated difficulty if able to mine a block or not, will update the nonce every iteration. With random nonce
    def p_o_w(self, block):
        block.nonce = 0
        get_hash = block.generate_hash() #generate hash
        while not get_hash.startswith("0" * Blockchain.difficulty): #check if it matches our difficulty requirement
            block.nonce += 1 #generate a random nonce
            get_hash = block.generate_hash() #generate hash
        return get_hash

    #validity helper method; checks if hash has enough difficulty and matches the hash
    def is_valid(self, block, block_hash):

        if block_hash.startswith("0" * Blockchain.difficulty):
            if block.generate_hash() == block_hash:
                return True
        return False

    # Returns the last Block in the Blockchain
    def last_block(self):
        return self.chain[-1]
