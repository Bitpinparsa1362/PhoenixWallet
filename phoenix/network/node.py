import socket
import threading
import json
import time


class PeerManager:
    def __init__(self):
        self.peers = set()

    def add_peer(self, host, port):
        self.peers.add((host, port))

    def get_peers(self):
        return list(self.peers)


class Node:
    def __init__(self, host="127.0.0.1", port=5000):
        self.host = host
        self.port = port
        self.peers = PeerManager()
        self.transactions = []
        self.seen_blocks = set()

    # ---------------- TRANSACTION ----------------
    def add_transaction(self, tx):
        self.transactions.append(tx)
        print("[TX] Transaction added:", tx)

    # ---------------- START NODE ----------------
    def start(self):
        print("[NODE] Starting thread...")
        thread = threading.Thread(target=self.start_server)
        thread.daemon = True
        thread.start()

    # ---------------- SERVER ----------------
    def start_server(self):
        print("[NODE] Server starting...")

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        try:
            server.bind((self.host, self.port))
            server.listen(5)
            print(f"[NODE] Running on {self.host}:{self.port}")
        except Exception as e:
            print("[ERROR] bind failed:", e)
            return

        while True:
            try:
                client, addr = server.accept()
                data = client.recv(4096).decode()

                try:
                    message = json.loads(data)

                    # ---------------- HANDSHAKE ----------------
                    if message.get("type") == "handshake":
                        self.peers.add_peer(message["host"], message["port"])
                        print("[NEW PEER]", message)
                        client.close()
                        continue

                    # ---------------- BLOCK ----------------
                    if message.get("type") == "block":
                        block_hash = message.get("hash")

                        if block_hash in self.seen_blocks:
                            print("[SKIP] duplicate block")
                            client.close()
                            continue

                        self.seen_blocks.add(block_hash)

                        print("[RECEIVED BLOCK]", message)

                        self.broadcast(message)


                except Exception as e:
                    print("[ERROR] invalid message:", e)

                client.close()

            except Exception as e:
                print("[ERROR] server loop:", e)

    # ---------------- SEND ----------------
    def send_block(self, host, port, message):
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((host, port))
            client.send(json.dumps(message).encode())
            client.close()
        except Exception as e:
            print(f"[ERROR] send failed {host}:{port} -> {e}")

    # ---------------- BROADCAST ----------------
    def broadcast(self, message):
        if message.get("hash") in self.seen_blocks:
            return

        self.seen_blocks.add(message.get("hash"))

        print("[NODE] Broadcasting block...")

        for host, port in self.peers.get_peers():
            self.send_block(host, port, message)
