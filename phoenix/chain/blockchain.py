from phoenix.chain.block import Block


class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.block_hash_set = set()

        genesis = Block(0, [], "0")
        self.chain.append(genesis)
        self.block_hash_set.add(genesis.hash)

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def add_block(self, block):
        if block.hash in self.block_hash_set:
            print("Duplicate block ignored.")
            return False

        self.chain.append(block)
        self.block_hash_set.add(block.hash)
        return True

    def mine_block(self):
        block = Block(
            len(self.chain),
            self.pending_transactions,
            self.chain[-1].hash
        )

        self.add_block(block)
        self.pending_transactions = []
        return block
