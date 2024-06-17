import rpyc
from services.search import Searcher

class SlaveService(rpyc.Service):
    def __init__(self):
        self.ip, self.port =  rpyc.discover("DATA")[0]
        self.conn = rpyc.connect(self.ip, self.port)

        self.searcher = Searcher()

    def exposed_search(self):
        pass
        #return f"Returning the search from the {self.__class__.__name__}"

    def exposed_show_all(self):
        data = self.conn.root.get_data()
        return self.searcher.show_all(data)
    
def create_slave(name):
    return type(name, (SlaveService,), {})
