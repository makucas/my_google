import json
import rpyc
from rpyc.utils.server import ThreadedServer

class DataService(rpyc.Service):
    def __init__(self, data_path):
        self.data_path = data_path
        self.data = None
        self.exposed_load_data()

    def exposed_load_data(self):
        with open(self.data_path, 'r') as json_file:
            self.data = json.load(json_file)

    def exposed_save_data(self, new_data):
        for i in range(len(new_data)):
            new_data[i]["index"] = i
        with open(self.data_path, 'w') as json_file:
            json.dump(new_data, json_file)

    def exposed_insert_file(self, archive_path):
        try:
            with open(archive_path, 'r') as json_file:
                new_archive = json.load(json_file)
                new_archive["index"] = len(self.data)    
        except:
            return False
        
        self.data.append(new_archive)
        self.save_data(self.data)
        return True
    
    def exposed_remove_file(self, index):
        try:
            del self.data[index]
            self.save_data(self.data)
            return True
        except:
            return False
        
    def exposed_get_data(self):
        return self.data
        
if __name__ == "__main__":
    #d = DataService("../dataset/sample_dataset.json")
    #d.load_data()
    #print(d.data)
    
    server = ThreadedServer(DataService("../dataset/sample_dataset.json"), port=18813)
    server.start()
