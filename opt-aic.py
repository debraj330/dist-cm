# optical-aic.py
import zmq
import time

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)   # request socket
    socket.connect("tcp://optical-node:5555")  # connect to node container service

    while True:
        instruction = "PRINT_HELLO"
        print(f"[AIC] Sending instruction: {instruction}")
        socket.send_string(instruction)

        reply = socket.recv_string()
        print(f"[AIC] Received reply: {reply}")

        time.sleep(2)  # send every 2 seconds

if __name__ == "__main__":
    main()
