import rpyc

ip, port = rpyc.discover("MASTER")[0]
c = rpyc.connect(ip, port)
size, composed_string = c.root.show_all()
print(composed_string)