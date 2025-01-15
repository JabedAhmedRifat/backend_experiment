import socket

# Server settings
HOST = "127.0.0.1"  # Localhost
PORT = 12345        # Port to connect to

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        # Take input from the user
        message = input("Enter message to send (or type 'exit' to quit): ")
        if message.lower() == 'exit':
            print("Exiting client...")
            break

        # Send the message to the server
        sock.sendto(message.encode(), (HOST, PORT))

        # Receive response from the server
        response, server_address = sock.recvfrom(1024)
        print(f"Received from server: {response.decode()}")
finally:
    sock.close()

