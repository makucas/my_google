import rpyc
from modules.search import Searcher

class SlaveService(rpyc.Service):
    def __init__(self):
        self.ip, self.port =  rpyc.discover("DATA")[0]
        self.conn = rpyc.connect(self.ip, self.port)

        self.searcher = Searcher()

    def exposed_search(self, search_string):
        data = self.conn.root.get_data()
        index_list = self.searcher.search(data, search_string)
        size, composed_string = self.searcher.show(data, index_list)
        return size, composed_string
    
    def exposed_show_instance(self, index):
        data = self.conn.root.get_data()
        composed_string = self.searcher.show_instance(data, index)
        return composed_string

    def exposed_show_all(self):
        data = self.conn.root.get_data()
        return self.searcher.show_all(data)
    
def create_slave(name):
    return type(name, (SlaveService,), {})
