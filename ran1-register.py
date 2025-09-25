# ------------------------------
# File: ran1-register.py (updated)
# ------------------------------
import zmq

VALID_AIC_ID = "01"
VALID_NODE_ID = "N01"

def start_register():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://127.0.0.1:6000")

    print("[Register] RAN1 Register started... Waiting for AIC or Node registration requests.")

    while True:
        message = socket.recv_json()
        
        if "aic_id" in message:  # AIC registration
            aic_id = message.get("aic_id")
            print(f"[Register] Received AIC registration with ID: {aic_id}")
            if aic_id == VALID_AIC_ID:
                socket.send_json({"status": "REGISTRATION_SUCCESS"})
                print("[Register] AIC registration successful.")
            else:
                socket.send_json({"status": "REGISTRATION_FAILED"})
                print("[Register] AIC registration failed.")
        
        elif "node_id" in message:  # Node registration
            node_id = message.get("node_id")
            print(f"[Register] Received Node registration with ID: {node_id}")
            if node_id == VALID_NODE_ID:
                socket.send_json({"status": "NODE_REGISTRATION_SUCCESS"})
                print("[Register] Node registration successful.")
            else:
                socket.send_json({"status": "NODE_REGISTRATION_FAILED"})
                print("[Register] Node registration failed.")
