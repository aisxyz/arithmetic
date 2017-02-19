# coding: utf8

class LinkHashTable:
    def __init__(self, maxsize=9):
        self.maxsize = maxsize
        self.hash_table_container = []
        for _ in range(maxsize):
            self.hash_table_container.append([])

    def get_hash_table_container(self):
        return self.hash_table_container
    
    def insert(self, item):
        hash_index = item % self.maxsize
        self.hash_table_container[hash_index].append(item)

    def delete(self, item):
        hash_index = item % self.maxsize
        self.hash_table_container[hash_index].remove(item)

    def search(self, item):
        hash_index = item % self.maxsize
        index_in_hash_table = self.hash_table_container[hash_index].index(item)
        return(hash_index, index_in_hash_table)


# Example use:
if __name__ == '__main__':
    table = LinkHashTable()
    print('Start:', table.get_hash_table_container())
    datas = [5, 28, 19, 15, 20, 33, 12, 17, 10]
    print('Insert:', datas)
    for item in datas:
        table.insert(item)
    print(table.get_hash_table_container())
    print('Search datas[3]:', datas[3])
    print(table.search(datas[3]))
    print('Delete datas[3]:', datas[3])
    table.delete(datas[3])
    print(table.get_hash_table_container())
