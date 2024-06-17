import rpyc

c = rpyc.connect("localhost", "18813")
c.root.load_data()
print(c.root.get_data())