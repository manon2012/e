import socket

sk =  socket.socket()

addr = ('127.0.0.1',8000)

sk.bind(addr)


sk.listen(1)

while True:
    print "wait for connect"
    conn, add=sk.accept()
    print "server is running..."
    while True:
        print "%s is connected"%conn
        print "welcome"
        try:
            r=conn.recv(1024)
        except Exception, e:
            break
        print r
        if r =="": # client break before send
            print "client %s is disconnected."%conn
            break

        inp = raw_input(">>>>>")
        try:
            conn.send(inp)
        except Exception:
            break
