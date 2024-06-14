from rpyc.utils.server import ThreadedServer
import threading
import slave
import rpyc

class MasterService(rpyc.Service):
    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass

    def exposed_search(self): 
        ip, port = rpyc.discover("SLAVE")[0]
        c = rpyc.connect(ip, port)
        result = c.root.search()
        return result

def run_server(service, port):
    server = ThreadedServer(service, port=port, auto_register=True)
    print(f"Servidor {service.__name__} iniciado na porta {port}")
    server.start()

if __name__ == "__main__":
    slave_1 = slave.create_slave("Slave1Service")
    slave_2 = slave.create_slave("Slave2Service")
    slave_3 = slave.create_slave("Slave3Service")

    thread1 = threading.Thread(target=run_server, args=(MasterService, 18812))
    thread2 = threading.Thread(target=run_server, args=(slave_1, 18813))
    thread3 = threading.Thread(target=run_server, args=(slave_2, 18814))
    thread4 = threading.Thread(target=run_server, args=(slave_3, 18815))

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
