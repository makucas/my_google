import rpyc

class SimpleBalancing():
    def __init__(self):
        self.slaves = ["SLAVE1", "SLAVE2", "SLAVE3"]
        self.index = 0

    def update_index(self):
        if self.index == 2:
            self.index = 0
        else:
            self.index +=1

    def return_connection(self):
        slave_name = self.slaves[self.index]
        ip, port =  rpyc.discover(slave_name)[0]
        self.update_index()
        return ip, port, slave_name
    
if __name__ == "__main__":
    b = SimpleBalancing()
    for i in range(4):
        print(b.return_connection())