
import socket

ser = socket.socket()
ser.bind(('localhost',2000))
ser.listen(3)

while True:
    
    conn,addr = ser.accept()

    while True:
        try:
            data=conn.recv(1024)
        except Exception,e:
            print e
            break
        else:
            if data=="":break
            else:print data
        data=raw_input(">>")
        conn.send(data)


