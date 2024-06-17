from rpyc.utils.server import ThreadedServer
from nodes.master_node import MasterService
from nodes.data_node import DataService
import nodes.slave_node as slave_node
import threading

MASTER_PORT = 18812
DATA_PORT = 18813
SLAVE_PORT = 18814

def start_server(service, port):
    server = ThreadedServer(service, port=port, auto_register=True)
    #print(f"Servidor {service.__name__} iniciado na porta {port}")
    print("starting...")
    server.start()

def start_thread(service, port):
    thread = threading.Thread(target=start_server, args=(service, port))
    thread.start()
    return thread

if __name__ == "__main__":
    # Criando dinamicamente os SlaveServices
    slave_services = ["Slave1Service", "Slave2Service", "Slave3Service"]
    slaves = [slave_node.create_slave(service) for service in slave_services]

    threads = []

    # Iniciando o DB
    threads.append(start_thread(DataService("dataset/sample_dataset.json"), DATA_PORT))

    # Iniciar servidor mestre
    threads.append(start_thread(MasterService, MASTER_PORT))

    # Iniciar servidores escravos
    for i, slave in enumerate(slaves, start=1):
        threads.append(start_thread(slave, SLAVE_PORT + i))

    # Aguardar todas as threads terminarem
    for thread in threads:
        thread.join()

