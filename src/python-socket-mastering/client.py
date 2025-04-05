import socket


FORMAT = 'utf-8' # Encoding format for messages
HEADER = 64 # Size of the header for messages
PORT = 5050
DISCONNECT_MESSAGE = "!DISCONNECT" # Message to disconnect from the server
SERVER = socket.gethostbyname(socket.gethostname()) # Get the local machine hostname
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a TCP socket
client.connect(ADDR) # Connect to the server using the address and port

def send(msg):
    message = msg.encode(FORMAT) # Encode the message to bytes
    msg_length = len(message) # Get the length of the message
    send_length = str(msg_length).encode(FORMAT) # Encode the length of the message to bytes
    send_length += b' ' * (HEADER - len(send_length)) # Pad the length with spaces to fit the header size
    client.send(send_length) # Send the length of the message to the server
    client.send(message) # Send the message to the server
    print(client.recv(2048).decode(FORMAT)) # Receive acknowledgment from the server and decode it


send("Hello World!") # Send a message to the server
send("Hello World!")
send("Hello World!")
send(DISCONNECT_MESSAGE)