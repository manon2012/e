import  socket


print "client..."

addr =('127.0.0.1',8000)
sk = socket.socket()


sk.connect(addr)
print "i am %s"%sk
while True:

    inp = raw_input(">>>>>>>>>")
    if inp =="":continue
    if inp =="exit":
        break
    sk.send(inp)

    print sk.recv(1024)