import time
import hashlib

class Block:
    def __init__(self, index, transactions, previous_hash, difficulty=4):
        self.index = index
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.timestamp = time.time()
        self.nonce = 0
        self.difficulty = difficulty
        self.hash = self.mine()

    def calculate_hash(self):
        data = str(self.index) + str(self.transactions) + str(self.previous_hash) + str(self.timestamp) + str(self.nonce)
        return hashlib.sha256(data.encode()).hexdigest()

    def mine(self):
        target = "0" * self.difficulty

        while True:
            hash_value = self.calculate_hash()
            if hash_value.startswith(target):
                return hash_value
            self.nonce += 1
