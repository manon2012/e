import socket

conn= socket.socket()

conn.connect(('localhost',2000))

while True:
    data= raw_input(">>")
    if data == "": continue
    if data == "exit": break
    conn.send(data)

    print conn.recv(1024)