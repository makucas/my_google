import rpyc

ip, port = rpyc.discover("MASTER")[0]
c = rpyc.connect(ip, port)
print(c.root.search())