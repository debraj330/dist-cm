# ------------------------------
# File: ran1-node.py
# ------------------------------
import zmq
import random
import time

NODE_ID = "N01"

def register_with_ran():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://127.0.0.1:6000")  # Register service at port 6000

    print(f"[Node-{NODE_ID}] Attempting to register with Register...")

    socket.send_json({"node_id": NODE_ID})

    try:
        response = socket.recv_json()
        if response.get("status") == "NODE_REGISTRATION_SUCCESS":
            print(f"[Node-{NODE_ID}] Successfully registered with Register.")
            return True
        else:
            print(f"[Node-{NODE_ID}] Registration failed.")
            return False
    except Exception as e:
        print(f"[Node-{NODE_ID}] ERROR: {e}")
        return False

def listen_for_commands():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://127.0.0.1:6002")  # Listen to broker on port 6002
    socket.setsockopt_string(zmq.SUBSCRIBE, "")  # Subscribe to all messages

    print(f"[Node-{NODE_ID}] Listening for commands from Broker...")

    while True:
        message = socket.recv_string()
        try:
            val = int(message)
            if val in [100, 101, 102, 103]:
                print(f"[Node-{NODE_ID}] Received value: {val}")
            else:
                while True:
                    sinr = round(random.uniform(10, 20), 2)
                    cqi = random.randint(5, 10)
                    mcs = random.randint(0, 28)
                    print(f"[Node id={NODE_ID}, SINR={sinr}, CQI={cqi}, MCS={mcs}]")
                    time.sleep(1)
        except ValueError:
            print(f"[Node-{NODE_ID}] Invalid message received: {message}")

if __name__ == "__main__":
    if register_with_ran():
        start_node = input("[Node] Start the node? (yes/no): ").strip().lower()
        if start_node == "yes":
            listen_for_commands()
        else:
            print("[Node] Node not started.")

