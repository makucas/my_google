from nodes.data_node import DataManager
from search import Searcher

d = DataManager("../dataset/sample_dataset.json")
d.load_data()

s = Searcher(d.data)
#size, composed_string = s.show_all()
index_list = s.search("Hoje")
size, string = s.show(index_list)
print(string)

