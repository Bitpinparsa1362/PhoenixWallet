import subprocess
import time

print("Starting Phoenix Network...")

# Node 5000
p1 = subprocess.Popen(["python", "-m", "phoenix.network.node"])

time.sleep(1)

# Node 5002
p2 = subprocess.Popen(["python3", "node2.py"])

time.sleep(1)

print("Nodes started!")
print("Now run: python3 main.py")

try:
    p1.wait()
    p2.wait()
except KeyboardInterrupt:
    print("Shutting down network...")
