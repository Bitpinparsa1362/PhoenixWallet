from phoenix.chain.blockchain import Blockchain
from phoenix.core.transaction import Transaction

bc = Blockchain()

tx1 = Transaction("Alice", "Bob", 10)
tx2 = Transaction("Bob", "Charlie", 5)

bc.add_transaction(tx1)
bc.add_transaction(tx2)

block = bc.mine_block()

print("Height:", len(bc.chain))
print("Hash:", block.hash)
print("Transactions:", len(block.transactions))
