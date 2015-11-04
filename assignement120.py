# use sockets to retreive url and display headers

# create socket
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to socket
mysock.connect(('www.py4inf.com', 80))
# send data over socket to webserver
mysock.send ('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

while True :
    data = mysock.recv(512)
    if len(data) < 1 :
        break
    print data

# close socket
mysock.close()
