class PeerManager:
    def __init__(self):
        self.peers = set()

    def add_peer(self, host, port):
        self.peers.add((host, port))

    def remove_peer(self, host, port):
        self.peers.discard((host, port))

    def get_peers(self):
        return list(self.peers)
