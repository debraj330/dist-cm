# ------------------------------
# File: ran1-aic.py
# ------------------------------
import zmq
import sys

AIC_ID = "01"  # The ID of this AI Controller

def register_with_ran():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://192.168.0.178:6000")  # Connect to Register on port 6000

    print(f"[AIC-{AIC_ID}] Attempting to register with Register...")

    socket.send_json({"aic_id": AIC_ID})

    try:
        response = socket.recv_json()
        if response.get("status") == "REGISTRATION_SUCCESS":
            print(f"[AIC-{AIC_ID}] Successfully registered with Register.")
            return True
        else:
            print(f"[AIC-{AIC_ID}] Registration failed.")
            return False
    except Exception as e:
        print(f"[AIC-{AIC_ID}] ERROR: {e}")
        return False

if __name__ == "__main__":
    if register_with_ran():
        print(f"[AIC-{AIC_ID}] Hosting xApp1, xApp2, rApp1, rApp2...")
        print("[AIC] Ready to execute commands.")
    else:
        sys.exit(1)

