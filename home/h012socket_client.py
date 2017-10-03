import socket

conn= socket.socket()

conn.connect('localhost',2000)

conn.send("hihi")

print conn.recv(1024)