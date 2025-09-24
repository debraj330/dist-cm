# ------------------------------
# File: ran1-register.py
# ------------------------------
import zmq

VALID_AIC_ID = "01"  # Only this AIC ID is considered valid

def start_register():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://192.168.0.178:6000")  # Register listens on port 6000

    print("[Register] RAN1 Register started... Waiting for AIC registration requests.")

    while True:
        message = socket.recv_json()
        aic_id = message.get("aic_id")
        print(f"[Register] Received registration request with AIC ID: {aic_id}")

        if aic_id == VALID_AIC_ID:
            print("[Register] Valid AIC registered successfully.")
            socket.send_json({"status": "REGISTRATION_SUCCESS"})
        else:
            print("[Register] Invalid AIC ID! Registration failed.")
            socket.send_json({"status": "REGISTRATION_FAILED"})

if __name__ == "__main__":
    start_register()

