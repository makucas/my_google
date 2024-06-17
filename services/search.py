class Searcher():        
    def search(self, search_string):
        index_list = []
        for i, article in enumerate(self.data):
            analysed_text = f"{article['title'].lower()} {article['text'].lower()}".split()
            if search_string.lower() in analysed_text:
                index_list.append(i)
        return index_list

    def show(self, index_list):
        composed_string = ""
        for index in index_list:
            composed_string += f"{self.data[index]['index']}: {self.data[index]['title']}\n"
        return len(index_list), composed_string

    def show_instance(self, index):
        instance = self.data[index]
        return(f"Título: {instance['title']}\nAutor: {instance['authors']}\n\n{instance['text']}")
    
    def show_all(self, data):
        composed_string = ""

        target_data = data[0:50] if len(data) > 50 else data
        for article in target_data:
            composed_string += f"{article['index']}: {article['title']}\n"

        return len(data), composed_string
     

