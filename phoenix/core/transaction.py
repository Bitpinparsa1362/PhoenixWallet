import secrets
import time
import hashlib
import json

class Transaction:
    def __init__(self, sender, receiver, amount):
        self.id = secrets.token_hex(16)
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = time.time()
        self.signature = None

    def sign(self, signature):
        self.signature = signature

    def to_dict(self):
        return {
            "id": self.id,
            "sender": self.sender.address,
            "receiver": self.receiver.address,
            "amount": self.amount,
            "timestamp": self.timestamp,
            "signature": self.signature
        }

    def hash(self):
        tx = json.dumps(self.to_dict(), sort_keys=True)
        return hashlib.sha256(tx.encode()).hexdigest()
