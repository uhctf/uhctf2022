import socket
import os
import sys
from _thread import *
from threading import *
import gen
import time

FLAG = os.environ['FLAG']

ServerSideSocket = socket.socket()
host = '0.0.0.0'
port = int(sys.argv[1])

try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Socket is listening..')
ServerSideSocket.listen(5)

treshold = int(os.environ['TRESHOLD'])

def multi_threaded_client(connection, addr):
    a, key = gen.generate()
    t = time.time_ns()
    print(addr, ":", key)
    print(key)
    connection.send(str.encode(a))
    data = connection.recv(2048)
    response = data.decode('utf-8')
    if response.strip("\n") == key and time.time_ns()-t < treshold:
        connection.sendall(str.encode("That's correct here's the flag!\n" + FLAG + "\n"))
    elif response.strip("\n") == key:
        connection.sendall(str.encode("That was correct but try being faster ;)\n"))
    else:
        connection.sendall(str.encode("That's wasn't right!\n"))
    connection.close()

def main():
    ThreadCount = 0
    while True:
        Client, address = ServerSideSocket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        t = Thread(target = multi_threaded_client, args = (Client, address) )
        t.start()
        print(time.thread_time_ns())
        ThreadCount += 1
        print('Thread Number: ' + str(ThreadCount))
    ServerSideSocket.close()

if __name__ == '__main__':
	main()
