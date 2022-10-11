from hash_quad import *
import string

class Concordance:

    def __init__(self):
        self.stop_table = None          # hash table for stop words
        self.concordance_table = None   # hash table for concordance

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""

        stop_hash = HashTable(191)

        my_file = open(filename, 'r')
        for line in my_file.readlines():
            newline = line.strip()
            stop_hash.insert(newline)
        my_file.close()
        self.stop_table = stop_hash




    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""

        concordance_hash = HashTable(191)
        stop_table = self.stop_table
        my_file = open(filename, 'r')

        curr_line = 0

        # remove the punctuation from each line and call the punctuation-free line my_line_copy
        for my_line in my_file.readlines():
            curr_line += 1
            my_line_copy = my_line.strip()
            for letter in my_line_copy:
                if letter == "'":
                    my_line_copy = my_line_copy.replace(letter, '')
                elif letter in string.punctuation:
                    my_line_copy = my_line_copy.replace(letter, ' ')
                elif 65 <= ord(letter) <= 90: #remove uppercase letters
                    lowercase = chr(ord(letter) + 32)
                    my_line_copy = my_line_copy.replace(letter, str(lowercase))

            # create a list of all the valid tokens in the line that will be inserted into the concordance hash
            my_tokens = my_line_copy.split()
            valid_words = []
            for my_token in my_tokens: # for each token, remove them from the list if they are not words
                if my_token.isalpha():
                    if not stop_table.in_table(my_token):
                        valid_words.append(my_token)



            # insert all words into the concordance hash
            for word in valid_words:
                value = concordance_hash.get_value(word)
                if value is not None:
                    if value[len(value)-1] != curr_line:
                        concordance_hash.insert(word, value + [curr_line])
                else:
                    concordance_hash.insert(word, [curr_line])


        my_file.close()
        self.concordance_table = concordance_hash

    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""

        conc_entries = self.concordance_table

        # sort concordance entries alphabetically
        sort_list = []
        sorted_list = []
        for e in conc_entries.hash_table:
            if e is not None:
                sort_list.append(e)

        for i in range(len(sort_list)):

            minimum = sort_list[0]
            for e in sort_list:
                if e[0] < minimum[0]:
                    minimum = e
            sort_list.remove(minimum)
            sorted_list.append(minimum)


        # print concordance entries with correct formatting
        out_file = open(filename, 'w')

        for e in sorted_list:
            out_file.write(e[0] + ':')
            for line_number in e[1]:
                out_file.write(' '+str(line_number))
            if sorted_list.index(e) != len(sorted_list)-1:
                out_file.write('\n')

        out_file.close()










