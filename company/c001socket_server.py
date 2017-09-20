import socket
import os

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
        print "welcome,waitting for inp"
        try:
            r=conn.recv(1024)
        except Exception, e:
            break
        #print r
        # try:
        rr = os.popen(r).read()
        # except Exception:
        #     conn.send("cmd is invalid.")
        #     break

        print rr + "111"
        #if r =="": # client break before send
        if not rr:
            #print "client %s is disconnected."%conn
            print "222"
            conn.send("cmd is invalid")
            continue

        readsize = str(len(rr))
        print readsize +"333"
        conn.send(readsize)
        #inp = raw_input(">>>>>")
        try:
            conn.send(rr)
        except Exception:
            break
