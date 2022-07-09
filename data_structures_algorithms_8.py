#08 python dictionaries and hash tables

def get_index(hash_table, key):
    result = 0
    for string in key:
        result += ord(string)
    index = result % len(hash_table)
    return index

class BasicHashTable:
    def __init__(self, max_index=4096):
        self.hash_table = [None] * max_index

    def insert(self, key, value):
        self.hash_table[get_index(self.hash_table,key)] = key, value

    def find(self, key):
        if self.hash_table[get_index(self.hash_table,key)] is not None:
            return self.hash_table[get_index(self.hash_table,key)][1]
        else:
            return None

    def update(self, key, value):
        self.hash_table[get_index(self.hash_table, key)] = key, value

    def list_all(self):
        return [kv[0] for kv in self.hash_table if kv is not None]

'''
hash_table = BasicHashTable()
hash_table.insert('ali', 123345123)
hash_table.insert('sally', 78789789)
print(hash_table.find('ali'))
hash_table.update('ali', 999999)
print(hash_table.find('ali'))
print(hash_table.list_all())
'''

#handling collisions with linear probing
def get_valid_index(hash_table, key):
    result = 0
    for string in key:
        result += ord(string)
    index = result % len(hash_table)
    while hash_table[index] is not None:
        if hash_table[index][0] == key:
            return index
        index += 1
        if index > len(hash_table) - 1:
            index = 0
    if hash_table[index] is None:
        return index


class ProbingHashTable:
    def __init__(self, max_index=6):
        self.hash_table = [None] * max_index

    def insert(self, key, value):
        index = get_valid_index(self.hash_table, key)
        self.hash_table[index] = key, value

    def find(self, key):
        if self.hash_table[get_valid_index(self.hash_table, key)] is not None:
            return self.hash_table[get_valid_index(self.hash_table, key)][1]
        else:
            return None

    def update(self, key, value):
        self.hash_table[get_valid_index(self.hash_table, key)] = key, value

    def list_all(self):
        return [kv[0] for kv in self.hash_table if kv is not None]

'''
hash_table2 = ProbingHashTable()
hash_table2.insert('listen', 123345123)
hash_table2.insert('silent', 78789789)
hash_table2.insert('siletn', 123345123)
hash_table2.insert('silten', 78789789)
hash_table2.insert('isletn', 123345123)
hash_table2.insert('sliten', 78789789)
print(hash_table2.find('listen'))
print(hash_table2.find('silent'))
print(hash_table2.find('sliten'))
hash_table2.update('listen', 999999)
print(hash_table2.find('listen'))
print(hash_table2.list_all())
'''

class HashTable:
    def __init__(self, max_index=4096):
        self.hash_table = [None] * max_index

    @staticmethod
    def get_valid_index(hash_table, key):
        result = 0
        for string in key:
            result += ord(string)
        index = result % len(hash_table)
        while hash_table[index] is not None:
            if hash_table[index][0] == key:
                return index
            index += 1
            if index > len(hash_table) - 1:
                index = 0
        if hash_table[index] is None:
            return index

    def __setitem__(self, key, value):
        index = HashTable.get_valid_index(self.hash_table, key)
        self.hash_table[index] = key, value

    def __getitem__(self, item):
        if self.hash_table[get_valid_index(self.hash_table, item)] is not None:
            #print(get_valid_index(self.hash_table, item))
            return self.hash_table[get_valid_index(self.hash_table, item)][1]
        else:
            #print(get_valid_index(self.hash_table, item))
            return None

    def __len__(self):
        return len([kv[0] for kv in self.hash_table if kv is not None])

    def __iter__(self):
        return (kv[0] for kv in self.hash_table if kv is not None)

    def __repr__(self):
        pairs = [f'{repr(kv[0])} : {repr(kv[1])}' for kv in self.hash_table if kv is not None]
        from textwrap import indent
        joined = indent(',\n'.join(pairs), ' ')
        return '{\n' + f'{joined}' + '\n}'

    def __str__(self):
        return self.__repr__()

hash_table3 = HashTable()
hash_table3['aakash'] = 124356
hash_table3['jadhesh'] = 654321
hash_table3['tamil'] = 9999999
print(hash_table3['aakash'])
print(hash_table3['jadhesh'])
print(len(hash_table3))
print(list(hash_table3))
print(hash_table3)