import json

# OBJECTIVES
# 1. Get meaning and definitions for itself only
# 2. Include other common words
class Jmdict_JPN_Dictionary:

    is_dict_loaded = False
    # TODO: make a method to set a new dict file
    # maybe can also do a config file
    # so rather than changing dict file everytime using it,
    # the code will change the dict file in the config when changing new dict file
    # and the code will read the dict file from config and set it during init
    dict_file = "dict/jmdict-eng-3.6.1.json"

    version = None
    _words = None
    
    def __init__(self):

        self.word_to_find = None
        self.is_kanji: bool

        # word_dict: the dictionary of the word
        self._word_dict = None
        self._sense = None

        # kanji: the  kanji
        self.kanji = []
        # is the kanji common
        # kana
        self.kana = []
        # is the kana common
        # applies to which kanji
        # data about its definition
        self.gloss = {}

        # If the dict file is loaded already no need to load again
        if self.is_dict_loaded:
            return
        
        # Try load dict file
        try:
            with open(self.dict_file, encoding="utf-8") as file:
                data = json.load(file)

        except Exception as e:
            # Failure to load the dict file
            print("\nError when opening the dictionary file\n", e)
            return
        
        else:
            # Successfully loaded the dict file
            self.is_dict_loaded = True

        self.version = data["version"]

        self._words = data["words"]

    def __str__(self):

        print_me = ''

        for key, value in vars(self).items():
            if key[0] == '_':
                continue

            print_me += f'{key}: {value}\n\n'

        return print_me
    
    # TODO: prioritise kanji when searching with hiragana
    # so that it will set is_kanji as true rather than false
    def find_by_word(self, word_to_find):

        self.word_to_find = word_to_find

        for word in self._words:

            for var in word["kanji"]:

                if self.word_to_find == var["text"]:

                    self._word_dict = word
                    self.is_kanji = True

                    return True
                
            for var in word["kana"]:

                if self.word_to_find == var["text"]:

                    self._word_dict = word
                    self.is_kanji = False

                    return True
        
        return False
    
    def populate_definitions(self):

        for var_kanji in self._word_dict["kanji"]:

            if var_kanji["common"]:
                self.kanji.append(var_kanji["text"])

        for var_kana in self._word_dict["kana"]:

            if var_kana["common"]:
                self.kana.append(var_kana["text"])

        self._sense = self._word_dict["sense"]

        if self.is_kanji:
            applies_to_word = "appliesToKanji"
        else:
            applies_to_word = "appliesToKana"

        gloss_count = 1

        for sense_dict in self._sense:

            if self.word_to_find not in sense_dict[applies_to_word] and '*' not in sense_dict[applies_to_word]:
                continue
            
            for gloss_list in sense_dict["gloss"]:

                self.gloss.setdefault(gloss_count, []).append(gloss_list["text"])
            gloss_count += 1


def find_by_id(id):

    with open("dict/jmdict-eng-3.6.1.json", encoding="utf-8") as file:
        data = json.load(file)

    words = data["words"]

    for word in words:

        if word["id"] == id:
            return word
    return None

if __name__ == "__main__":

    test = Jmdict_JPN_Dictionary()

    # with open("dict/jmdict-eng-3.6.1.json", encoding="utf-8") as file:
        # data = json.load(file)

    # print(data["version"])

    # SHOULD WRITE A TEST TO TEST CASES LIKE:
    # 1 AND 2 for different gloss that applies
    # 3 AND 4 for taking the kanji since it is written in kanji
    # find_me = '速い' # 1
    # find_me = '早い' # 2
    # find_me = '大学' # 3
    # find_me = 'だいがく' # 4
    find_me = '交換'

    test.find_by_word(find_me)
    test.populate_definitions()
    print(test)

    # print(test.word_dict.keys())
    # print(test)

    # for sense in test.sense:
    #     print(sense)
    #     print()

    # print(test.sense)

    # words = data["words"]
    # print(len(words))

    # found = False
    # for word in words:

    #     for var in word["kanji"]:

    #         if find_me == var["text"]:
    #             print(var["text"])
    #             print(word["id"])
    #             found = True
        
    #     if found:
    #         break

    # for word in words:

    #     if word["id"] == "1413240":
    #         print(word)
    #         break

    # print(words[0].keys())
    # print(type(words[30]))
    # print(words[30]["kanji"])

    # json2_print(words[30])

    # print(type(words[30]["kanji"]))
    # print(type(words[30]["kana"]))
    # print(type(words[30]["sense"]))
    # print(len(words[30]["kanji"]))

    # index = 200
    # index = 222
    # index = 311
    # index = 555

    # kanji = words[index]["kanji"]
    # print(kanji)
    # for var in kanji:
    #     print(var["text"])
    #     print(var["common"])

    # kana = words[index]["kana"]
    # print(kana)
    # for var in kana:
    #     print(var["text"])
    #     print(var["common"])
    #     for which_kanji in var["appliesToKanji"]:
    #         print(which_kanji)

    # sense = words[index]["sense"]
    # print(sense)
    # print(len(sense))
    # for var in sense:
    # #     print(var["text"])
    # #     print(var["common"])
    #     for which_kanji in var["appliesToKanji"]:
    #         print("appliesToKanji", which_kanji)

    #     for which_kanji in var["appliesToKana"]:
    #         print("appliesToKana", which_kanji)

    #     for which_kanji in var["related"]:
    #         print("related", which_kanji)

    #     for which_kanji in var["antonym"]:
    #         print("antonym", which_kanji)

    #     for which_kanji in var["field"]:
    #         print("field", which_kanji)

    #     for which_kanji in var["dialect"]:
    #         print("dialect", which_kanji)

    #     for which_kanji in var["misc"]:
    #         print("misc", which_kanji)

    #     for which_kanji in var["info"]:
    #         print("info", which_kanji)

    #     for gloss in var["gloss"]:
    #         print(gloss)

    #     print(var)

    #     print()

    # json2_print(words[index])