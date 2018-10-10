#!/usr/bin/python
import base64
import socket
import threading

bind_ip = '0.0.0.0'
bind_port = 9999

# set on TCP/IPv4
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# open socket
server.bind((bind_ip, bind_port))

# max connection = 5
server.listen(5)

print "[*] Listening on %s:%d" % (bind_ip, bind_port)

def handle_client(client_socket):
    request = client_socket.recv(1024)

    print "[*] Received: %s" % request
    plaintext = request.split('\r\n')[-2]
    ciphertext = base64.b64encode(plaintext)

    # response base64 encode string
    client_socket.send(ciphertext)
    client_socket.close()
    
while True:
    # get request
    client, addr = server.accept()
    print "[*] Acepted connection from: %s:%d" % (addr[0], addr[1])
    
    # create a thread to process request
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()

