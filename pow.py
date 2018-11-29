import utils

max_nonce = 4294967295
class Pow():
    def __init__(self, block):
        self.block = block
        self.target = 1 << (256 - block.bits)


    def prepare_data(self, nonce):
        data_list = [self.block.prev_block_hash,
                     self.block.data,
                     self.block.timestamp,
                     str(self.block.bits),
                     str(nonce)]
        return utils.encode(''.join(data_list))

    def run(self):
        nonce = 0
        while self.block.nonce < max_nonce:
            data = self.prepare_data(nonce)
            hash_hex = utils.sha256(data)
            print(hash_hex, end='\r', flush=True)
            if (int(hash_hex, 16) < self.target):
                print()
                break
            else:
                nonce += 1
        
        return nonce, hash_hex
        