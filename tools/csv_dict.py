import csv

class csv_dict:

    _csv_file = 'dict/wordlist_all.csv'
    _jpn_dict = []

    def __init__(self):

        self.found = []

        with open(self._csv_file, 'r', encoding='utf-8') as csv_file:

            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:

                self._jpn_dict.append(row)
    
    def __str__(self):

        for row in self._jpn_dict:
            print(row)

        return '\n'
    
    def find_by_word(self, find_me):

        for row in self._jpn_dict:

            if row['見出し'] == find_me:
                pass



if __name__ == "__main__":

    my_str = '大学'

    test = csv_dict()

    print(test)