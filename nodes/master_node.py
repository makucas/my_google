from load_balancing import SimpleBalancing
import rpyc

class MasterService(rpyc.Service):
    def __init__(self):
        self.lb = SimpleBalancing()

    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass

    def exposed_search(self): 
        ip, port, name = self.lb.return_connection()
        c = rpyc.connect(ip, port)
        result = c.root.search()
        return result
    
    def exposed_insert(self):
        ip, port, name = self.lb.return_connection()
        c = rpyc.connect(ip, port)
        result = c.root.search()
        return result

    def exposed_remove(self):
        ip, port, name = self.lb.return_connection()
        c = rpyc.connect(ip, port)
        result = c.root.search()
        return result

    def exposed_show_all(self):
        ip, port, name = self.lb.return_connection()
        c = rpyc.connect(ip, port)
        result = c.root.show_all()
        return result   
    