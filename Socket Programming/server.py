import socket #1 EndPoint of a 2 way communication.
import threading #Creates multiple threads (execution) within 1 program.

HEADER = 64 #ytes. First message to the client EVERYTIME.
#Communication endpoint, where it runs.
PORT = 5050 #Default for speed test servers. 
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT) #Binds them to an address.
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
"""
Uses IPv4 Address. Provides functionality for clients.
socket.gethostname() - Represents your computer.
SERVER = socket.gethostbyname(socket.gethostname()) = Your IPv4 Address.
"""

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
"""
socket.AF_INET - Tells the socket what type of Ip Address we're looking for.
socket.SOCK_STREAM - Streams data to the socket.
"""

server.bind(ADDR) #Anything that connects to this address will hit this socket.

def handle_client(conn, addr): #Handles individual connections between Client and Server.
    #It's in its own client so runs for each thread.
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        #Wait to recieve information from client.
        msg_length = conn.recv(HEADER).decode(FORMAT) #Stores the length of the 1st message. Converts from Byte to String.
        if msg_length:       
            msg_length = int(msg_length) #Converts to integer (length)
            msg = conn.recv(msg_length).decode(FORMAT) #Puts the length as the number of bytes.
            if msg == DISCONNECT_MESSAGE: #If the user wants to disconnect.
                connected = False

            print(f"[{addr}] {msg}")  # Outputs the address and the message.
            conn.send("Msg received".encode(FORMAT)) #Server sends message BACK to client.

    conn.close() #Ends the connection upon the user's request.

def start(): #Handles new connections and distributes them to where they need to go.
    server.listen()  # Look for new connections.
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept() #Waits for a new connection. Information about connection.
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}") #Tells us how many threads (clients) are acted on, in this process.

        """
        When a new connection occours:
            Pass to handle client.
            Give handle_client the connection and address.
            Start the thread.
        """

print("[STARTING] server is starting...") #Message for the user.
start() #Starts the server (calls the function).
