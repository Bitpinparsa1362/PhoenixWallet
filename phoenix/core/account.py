import secrets

class Account:
    def __init__(self):
        self.private_key = secrets.token_hex(32)
        self.public_key = "pub_" + self.private_key[:32]
        self.address = "PHX_" + self.public_key[-20:]
        self.balance = 0
        self.nonce = 0
