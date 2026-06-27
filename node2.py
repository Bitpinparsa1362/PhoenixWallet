from phoenix.network.node import Node
import time

node = Node(port=5002)
node.start()

print("Node 2 started.")

while True:
    time.sleep(1)
