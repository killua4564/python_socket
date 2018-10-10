#!/usr/bin/python
 
import socket
 
target_host = "0.0.0.0"
target_port = 9999

# set on TCP/IPv4
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get connection
client.connect((target_host, target_port))

# send request
client.send("GET / HTTP/1.1\r\nHost: 0.0.0.0:9999\r\njellyfish\r\n")
 
response = client.recv(4096)
 
print response