import socket #Endpoint for 2 way connection.

HEADER = 64  # ytes. First message to the client EVERYTIME.
#Communication endpoint, where it runs.
PORT = 5050  # Default for speed test servers.
SERVER = socket.gethostbyname(socket.gethostname()) #IP Address of machine.
ADDR = (SERVER, PORT)  # Binds them to an address.
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT" #Indicates that the user has disconnected.
ADDR = (SERVER, PORT) #Stored as Tuple

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Sets up the client.
client.connect(ADDR) #Connects to server.

def send(msg):  # A way for clients to send messages to the server.
    message = msg.encode(FORMAT) #Converts string to bytes
    msg_length = len(message) #Stores the length in a variable.
    send_length = str(msg_length).encode(FORMAT) #Converts to a string and encodes it, ready for sending.
    send_length += b' ' * (HEADER - len(send_length))  # Padding Bytespace.
    client.send(send_length) #Sends the length of the message from the client.
    client.send(message) #Sends the message from the client.
    print(client.recv(2048).decode(FORMAT)) #Arbritary.

send("Hello") #Sends the message.
send("Hi")
send(DISCONNECT_MESSAGE) #Disconnects.

#44:30 EXTENSION TASK?
#import pickle.
#For WAN - Republic IP Address. Change Server to hardocded.