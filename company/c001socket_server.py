import socket

sk =  socket.socket()

addr = ('127.0.0.1',8000)

sk.bind(addr)


sk.listen(3)

while True:
    conn, add=sk.accept()
    while True:
        print "server is running..."

        print "one connected is:", conn
        r=conn.recv(1024)
        print r
        # if r =="exit":  client break before send
        #     break

        inp = raw_input(">>>>>")
        conn.send(inp)
