import hashlib
import time
from datetime import datetime as dt

class Block(object):
    
    def __init__(self, data, previous_hash, previous_block):
        self.timestamp = time.time()
        self.data = data
        self.hash = self.calc_hash(data)
        self.previous_hash = previous_hash
        self.previous_block = previous_block
    
    def __repr__(self):
        s = "============================================== \n"
        s += "Current block: \n"
        s += "Data: {} \n".format(self.data)
        s += "Creation Time: {} \n".format(self.timestamp)
        s += "Hashcode: {} \n".format(self.hash)
        s += "Previous Block Hash: {} \n".format(self.previous_hash)
        s += "=============================================="
        return s
    
    @staticmethod
    def calc_hash(input_string):
        input_string = str(input_string).encode("utf-8")
        sha = hashlib.sha256()
        sha.update(input_string)
        return sha.hexdigest()
    
    @property
    def get_timestamp(self):
        return self.timestamp
    @property
    def get_hashcode(self):
        return self.hash
    @property
    def get_data(self):
        return self.data
    @property
    def get_prev_hashcode(self):
        return self.previous_hash
    
    @property
    def get_info(self):
        print("--- Require information about current block ---")
        req_info = input("Selection: 'timestamp', 'hashcode', 'prev_hashcode', 'data'", )
        req_info = str(req_info)
        if req_info == "timestamp":
            time = dt.fromtimestamp(self.timestamp).strftime("%Y-%m-%d, %H:%M:%S")
            return time
        elif req_info == "hashcode":
            return self.hash
        elif req_info == "prev_hashcode":
            return self.previous_hash
        elif req_info == "data":
            return self.data



class BlockChain(object):
    
    def __init__(self):
        """ Initializing BlockChain class:
            PARAMETERS
            ==========
            self.tail = end, to which blocks are appended
            self.num_blocks = updated, when new block is added
            """
        self.tail = None
        self.num_blocks = 0
    
    
    @property
    def chain_size(self):
        """ Return number of blocks in the blockchain"""
        return self.num_blocks
    
    
    def append_block(self, data):
        """ Appends a new block to the end of the chain. If chain is
            currently empty sets new node with previous_hash of 'None',
            else saves the previous hash and the previous block to the
            newly created block, then increases number of blocks.
            """
        
        assert data != None, "Data must not be of type None"
        if self.tail is None:
            prev_block = None
            prev_hash = None
        else:
            prev_block = self.tail
            prev_hash = self.tail.hash
        
        new_block = Block( data = data,
                          previous_hash = prev_hash,
                          previous_block = prev_block
                          )
            
                          self.tail = new_block
                          self.num_blocks += 1


def search_block(self, data):
    """ Search the blockchain for any given data and return
        the matching block. If data not found return None.
        """
            
            assert self.tail is not None, "Before searching, insert a block."
                curr_block = self.tail
                    while curr_block:
                        if curr_block.data == data:
                            return curr_block
                                curr_block = curr_block.previous_block
                                    print("Data not found in chain.")
                                    return None


def to_list(self):
    """  Copy the entire blockchain info into a python list object.
        """
            
            output = []
            curr_block = self.tail
                while curr_block:
                    info = [curr_block.data, curr_block.timestamp, curr_block.hash]
                    output.append(info)
                    curr_block = curr_block.previous_block
                        return output


### Testing ###

bc = BlockChain()
bc.append_block("cost: 10$, salary: 1000$, bank status: 5000$")
bc.append_block("cost: 1000$, salary: 1000$, bank status: 5000$")
bc.append_block("cost: 500$, salary: 2000$, bank status: 6500$")
bc.append_block("cost: 1000$, salary: 1200$, bank status: 6700$")
bc.append_block("cost: 1000$, salary: 1200$, bank status: 6900$")
bc.append_block("cost: 1000$, salary: 4000$, bank status: 9900$")
bc.append_block("cost: 2000$, salary: 0$, bank status: 7900$")

print(bc.to_list())
#[['cost: 2000$, salary: 0$, bank status: 7900$', 1605734858.9505548, 'c0575fd33ba4c905ba27f1153658b88aff15f04e2244fd4882eb32bf01ec59a3'], ['cost: 1000$, salary: 4000$, bank status: 9900$', 1605734858.950521, 'a3151d61c40d3315390c5929f22af9454d31cefd8889c75bf6ffe84f36197abc'], ['cost: 1000$, salary: 1200$, bank status: 6900$', 1605734858.950486, 'a1ccc1f2d1f426f0d130fb7299e252bc5bc68c0f5c6385e5857cd0d479740087'], ['cost: 1000$, salary: 1200$, bank status: 6700$', 1605734858.95045, '69ba9e3e281d99abb5b3b76ff46b7cd6d48d1fd11b0b040c16077213a2118830'], ['cost: 500$, salary: 2000$, bank status: 6500$', 1605734858.9504142, 'c79d76e8650b380d8939108916cd784d203fb4bb6653d244e84a72ac60387411'], ['cost: 1000$, salary: 1000$, bank status: 5000$', 1605734858.950376, 'ee1abcc4b3ca5f00495a1192083890d9f5766a018d08b5c0619f5b00cc4048fd'], ['cost: 10$, salary: 1000$, bank status: 5000$', 1605734858.950328, 'db6ec789a6f9c781eec606bfdb31d7331de4e302a185eb8ad683b2887a963108']]

print(bc.search_block(data="cost: 1000$, salary: 1200$, bank status: 6900$"))
#==============================================
#Current block:
#Data: cost: 1000$, salary: 1200$, bank status: 6900$
#Creation Time: 1605734905.040853
#Hashcode: a1ccc1f2d1f426f0d130fb7299e252bc5bc68c0f5c6385e5857cd0d479740087
#Previous Block Hash: 69ba9e3e281d99abb5b3b76ff46b7cd6d48d1fd11b0b040c16077213a2118830
#==============================================

print(bc.search_block(data="This data does not exist"))
#Data not found in chain.
#None
print("---")
print(bc.chain_size)
#7
print("---")
block = bc.search_block(data="cost: 1000$, salary: 1200$, bank status: 6900$")
print(block.previous_hash)
#69ba9e3e281d99abb5b3b76ff46b7cd6d48d1fd11b0b040c16077213a2118830
