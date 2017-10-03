
import socket

ser = socket.socket()
ser.bind(('localhost',2000))
ser.listen(3)

conn,addr = ser.accept()

data=conn.recv(1024)
conn.send(data.upper())