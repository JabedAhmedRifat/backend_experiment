import socket

HOST = "127.0.0.1"
PORT = 12345

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the address and port
sock.bind((HOST, PORT))
print(f"Server is running on {HOST}:{PORT}")

BUFFER_SIZE = 1024

try:
    while True:
        # Receive data from a client
        data, client_address = sock.recvfrom(BUFFER_SIZE)
        print(f"Received message: {data.decode()} from {client_address}")

        response = input("Enter message to send to client (or type 'exit' to stop): ")
        if response.lower() == "exit":
            print("Stopping server...")
            break
        sock.sendto(response.encode(), client_address)
except KeyboardInterrupt:
    print("Server shutting down...")
finally:
    sock.close()
