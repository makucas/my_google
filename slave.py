import rpyc

class SlaveService(rpyc.Service):
    def exposed_search(self):
        return "Returning the search from the slave"
    
def create_slave(name):
    return type(name, (SlaveService,), {})
