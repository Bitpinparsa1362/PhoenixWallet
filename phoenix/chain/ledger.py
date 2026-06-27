class Ledger:
    def __init__(self):
        self.accounts = {}
        self.transactions = []

    def add_account(self, account):
        self.accounts[account.address] = account

    def send(self, sender, receiver, amount):
        if sender.balance < amount:
            raise Exception("Not enough balance")

        sender.balance -= amount
        receiver.balance += amount

        from phoenix.core.transaction import Transaction

        tx = Transaction(sender, receiver, amount)
        tx.sign("dummy_signature")

        self.transactions.append(tx.to_dict())

        return tx
