import socket #Endpoint for 2 way connection.

HEADER = 64  # ytes. First message to the client EVERYTIME.
#Communication endpoint, where it runs.
PORT = 5050  # Default for speed test servers.
SERVER = socket.gethostbyname(socket.gethostname()) #IP Address of machine.
ADDR = (SERVER, PORT)  # Binds them to an address.
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
ADDR = (SERVER, PORT) #Stored as Tuple

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Sets up the client.
client.connect(ADDR) #Connects to server.


