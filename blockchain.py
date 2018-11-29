from block import Block
from utils import DB
import pickle

class Blockchain():
    def __init__(self):
        self.db = DB()
        if self.db.get('latest'):
            self.height = int(self.db.get('latest'))
            self.prev_block = pickle.loads(self.db.get(int(self.height)))
        else:
            new_block = Block(0, "Blockchain initialized!", "")
            self.prev_block = new_block.pow_on_block()
            self.db.put(0, pickle.dumps(self.prev_block))
            self.db.put('latest', 0)
            self.height = 0
    
    def add_block(self, data):
        new_block = Block(self.height + 1, data, self.prev_block.hash).pow_on_block()
        self.prev_block = new_block
        self.height = new_block.height
        self.db.put(self.prev_block.height, pickle.dumps(self.prev_block))
        self.db.put('latest', self.prev_block.height)

    def print_chain(self):
        for block_num in range(self.height + 1):
            self.print_block(block_num)


    def print_block(self, block_num):
        if block_num <= self.height:
            block = pickle.loads(self.db.get(block_num))
            print("#{0}".format(block.height))
            print("Timestamp: {0}".format(block.timestamp))
            print("Prev Hash : {0}".format(block.prev_block_hash))
            print("Data : {0}".format(block.data))
            print("Hash : {0}".format(block.hash))
        else:
            print("error: block {0} not found".format(block_num))
                