from phoenix.core.account import Account
from phoenix.chain.blockchain import Blockchain

bc = Blockchain()

a1 = Account()
a2 = Account()

tx = {
    "from": a1.address,
    "to": a2.address,
    "amount": 50
}

bc.add_transaction(tx)

block = bc.mine_block()

print("Block mined!")
print(block.hash)
print(block.transactions)
