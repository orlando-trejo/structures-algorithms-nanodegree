# @Author: otrejo
# @Date:   2020-03-05T00:12:05-05:00
# @Last modified by:   otrejo
# @Last modified time: 2020-03-27T20:27:09-04:00



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

def get_time():
    timestamp = time.gmtime()
    return (time.strftime("%Y-%m-%d %H:%M:%S", timestamp))


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

# Test 1
block_1 = Block(get_time(), "Block 1", 0)
block_2 = Block(get_time(), "Block 2", block_1)
block_3 = Block(get_time(), "Block 3", block_2)

print(block_1.data)
# "Block 1"
print(block_3.timestamp)
# Time in "%Y-%m-%d %H:%M:%S" format
print(block_3.previous_hash.data)
# "Block 2"

# Test 2
temp = BlockChain()
print(temp.head)
# None
print(temp.last)
# None

# Test 3
temp.add_block(get_time(), "Hello World")
temp.add_block(get_time(), "Blockchain!")
print(temp.last.data)
# "Blockchain!"
print(temp.last.previous_hash.data)
# "Hello World!"
