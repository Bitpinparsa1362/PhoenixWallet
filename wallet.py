import secrets
import hashlib

def create_wallet():
    private_key = secrets.token_hex(32)
    public_key = hashlib.sha256(private_key.encode()).hexdigest()
    address = "PHX" + hashlib.sha256(public_key.encode()).hexdigest()[:40]

    return private_key, public_key, address


if __name__ == "__main__":
    private_key, public_key, address = create_wallet()

    print("=== Phoenix Wallet ===")
    print("Address:")
    print(address)
    print()
    print("Public Key:")
    print(public_key)
    print()
    print("Private Key:")
    print(private_key)
