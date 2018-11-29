import datetime
from pow import Pow

class Block():
    def __init__(self, height, data, prev_block_hash):
        self.height = height
        self.prev_block_hash = prev_block_hash
        self.data = data
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        self.bits = 12
        self.nonce = 0
        self.hash = None
        
    def set_hash(self, hash):
        self.hash = hash

    def pow_on_block(self):
        pow_worker = Pow(self)
        self.nonce, self.hash = pow_worker.run()
        return self
        
    

