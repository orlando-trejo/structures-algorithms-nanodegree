import hashlib
import time

class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)

    def calc_hash(self, hash_str):
        sha = hashlib.sha256()
        #hash_str = "We are going to encode this string of data!".encode('utf-8')
        sha.update(hash_str.encode('utf-8'))
        return sha.hexdigest()

def get_utc_time():
    ts = time.gmtime()
    return (time.strftime("%Y-%m-%d %H:%M:%S", ts))


class BlockChain(object):

    def __init__(self):
        self.head = None
        self.last = None


    def add_block(self, timestamp, data):
        if self.head is None:
            self.head = Block(timestamp, data, 0)
            self.last = self.head
        else:
            current_last = self.last
            self.last = Block(timestamp, data, 0)
            self.last.previous_hash = current_last


block0 = Block(get_utc_time(), "Some Information", 0)
block1 = Block(get_utc_time(), "Another Information", block0)
block2 = Block(get_utc_time(), "Some more Information", block1)

print(block0.data)
print(block0.hash)
print(block0.timestamp)
print(block1.previous_hash.data)

temp = BlockChain()
temp.add_block(get_utc_time(), "Some Information")
temp.add_block(get_utc_time(), "Another Information")
print(temp.last.data)
print(temp.last.previous_hash.data)
