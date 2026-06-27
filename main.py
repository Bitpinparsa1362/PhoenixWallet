from phoenix.network.node import Node
import time

def main():
    print("PhoenixWallet is alive")

    # Node روی پورت اصلی شبکه
    node = Node(port=5001)
    node.start()

    time.sleep(2)

    # ---------------- TRANSACTION ----------------
    node.add_transaction({
        "sender": "PHX_ABC",
        "receiver": "PHX_XYZ",
        "amount": 10
    })

    time.sleep(2)

    # ---------------- BLOCK ----------------
    node.broadcast({
        "type": "block",
        "index": 1,
        "hash": "demo_hash_001",
        "transactions": 1
    })

    print("[MAIN] Done sending block")

if __name__ == "__main__":
    main()
