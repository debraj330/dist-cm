# optical-node.py
import zmq

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)   # reply socket
    socket.bind("tcp://*:5555")        # listens on port 5555

    print("[Node] Waiting for instructions...")
    while True:
        instruction = socket.recv_string()
        print(f"[Node] Received instruction: {instruction}")

        if instruction == "PRINT_HELLO":
            print("Hello World")  # task execution

        socket.send_string("ACK")  # acknowledge

if __name__ == "__main__":
    main()
