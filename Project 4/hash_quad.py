class HashTable:

    def __init__(self, table_size):  # can add additional attributes
        self.table_size = table_size  # initial table size
        self.hash_table = [None] * table_size  # hash table
        self.num_items = 0  # empty hash table

    def insert(self, key, value=None):
        ''' Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is any object (e.g. Python List).
        If the key is not already in the table, the key is inserted along with the associated value
        If the key is in the table, the new value replaces the existing value.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1).'''
        key_spot = self.get_index(key)
        # if there's already a spot containing this key, put in the new value:
        if key_spot is not None:
            self.hash_table[key_spot] = [key, value]
            return


        # determine ideal key index
        ideal_loc = self.horner_hash(key)
        # if ideal spot is available, insert key and value there
        if self.hash_table[ideal_loc] is None:
            self.hash_table[ideal_loc] = [key, value]
            self.num_items += 1
        # deal with collisions using quadratic probing
        else:
            next_loc = ideal_loc
            i = 0
            while self.hash_table[next_loc] is not None:
                next_loc = (ideal_loc + i ** 2) % self.table_size
                i += 1
            self.hash_table[next_loc] = [key, value]
            self.num_items += 1

        # if the load factor is greater than .5, increase table size and rehash.
        if self.get_load_factor() > .5:
            old = self.hash_table
            self.table_size = 2 * self.table_size + 1
            self.hash_table = [None] * self.table_size
            self.num_items = 0
            for entry in old:
                if entry is not None:
                    self.insert(entry[0], entry[1])

    def horner_hash(self, key):
        ''' Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification.'''

        if len(key) < 8:
            n = len(key)
        else:
            n = 8
        sum = 0
        i = 0
        for letter in key:
            sum += ord(letter) * 31 ** (n - 1 - i)
            i += 1

        return int(sum % self.table_size)

    def in_table(self, key):
        ''' Returns True if key is in an entry of the hash table, False otherwise.'''
        if self.get_index(key) is not None:
            return True
        else:
            return False

    def get_index(self, key):
        ''' Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None.'''
        old_guess = self.horner_hash(key)
        new_guess = old_guess
        i = 0
        while self.hash_table[new_guess] is not None:
            if self.hash_table[new_guess][0] == key:
                return new_guess
            else:
                new_guess = (old_guess + i ** 2) % self.table_size
                i += 1
        return None


    def get_all_keys(self):
        ''' Returns a Python list of all keys in the hash table.'''
        return [slot[0] for slot in self.hash_table if slot is not None]

    def get_value(self, key):
        ''' Returns the value associated with the key. 
        If key is not in hash table, returns None.'''
        index = self.get_index(key)
        if index is None:
            return None
        else:
            return self.hash_table[index][1]

    def get_num_items(self):
        ''' Returns the number of entries in the table.'''
        return self.num_items

    def get_table_size(self):
        ''' Returns the size of the hash table.'''
        return self.table_size

    def get_load_factor(self):
        ''' Returns the load factor of the hash table (entries / table_size).'''
        return self.num_items / self.table_size
