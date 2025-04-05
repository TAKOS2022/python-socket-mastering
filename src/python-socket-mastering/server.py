import socket
import threading

FORMAT = 'utf-8' # Encoding format for messages
HEADER = 64 # Size of the header for messages
PORT = 5050
DISCONNECT_MESSAGE = "!DISCONNECT" # Message to disconnect from the server
SERVER = socket.gethostbyname(socket.gethostname()) # Get the local machine hostname
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a TCP socket
server.bind(ADDR) # Bind the socket to the address and port


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) # Receive message from client -- 1024 bytes max that can be received at once
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            conn.send("Message received".encode(FORMAT)) # Send acknowledgment to the client
    conn.close() # Close the connection when done

def start():
    server.listen() # Listen for incoming connections
    print(f"[LISTENING] Server is listening on {SERVER}:{PORT}")
    while True:
        conn, addr = server.accept() # Accept a new connection
        thread = threading.Thread(target=handle_client, args=(conn, addr)) # Create a new thread for the client
        thread.start() # Start the thread
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}") # Print the number of active connections (-1 for the main thread)

if __name__ == "__main__":
    print("[STARTING] Server is starting...")
    start() # Start the server