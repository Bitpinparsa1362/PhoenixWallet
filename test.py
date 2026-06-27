from phoenix.core.account import Account
from phoenix.chain.ledger import Ledger

ledger = Ledger()

a1 = Account()
a2 = Account()

a1.balance = 100

ledger.add_account(a1)
ledger.add_account(a2)

tx = ledger.send(a1, a2, 30)

print("A1:", a1.balance)
print("A2:", a2.balance)
print(tx.to_dict())
