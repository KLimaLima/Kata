import json

# OBJECTIVES
# 1. Get meaning and definitions for itself only
# 2. Include other common words
class JPN_Dictionary:

    loaded_dict = False
    
    version = None
    _words = None
    
    def __init__(self, dict_file):

        # word_dict: the dictionary of the word
        self.word_dict = None
        # kanji: the  kanji
        self.kanji = None
        # is the kanji common
        # kana
        self.kana = None
        # is the kana common
        # applies to which kanji
        # data about its definition
        self.gloss = None
        self.sense = None

        if self.loaded_dict:
            return
        # TODO: what if wants to use another dict file
            
        with open(dict_file, encoding="utf-8") as file:
            data = json.load(file)
        
        self.loaded_dict = True

        self.version = data["version"]

        self._words = data["words"]

    def __str__(self):

        print_me = ''

        for key, value in vars(self).items():
            if key[0] == '_':
                continue

            print_me += f'{key}: {value}\n\n'

        return print_me
        
    def find_by_word(self, find_me):

        for word in self._words:

            for var in word["kanji"]:

                if find_me == var["text"]:

                    self.word_dict = word

                    return True
        
        return False
    
    def populate_definitions(self):

        self.kanji = self.word_dict["kanji"]
        self.kana = self.word_dict["kana"]
        self.sense = self.word_dict["sense"]

def find_by_id(id):

    with open("dict/jmdict-eng-3.6.1.json", encoding="utf-8") as file:
        data = json.load(file)

    words = data["words"]

    for word in words:

        if word["id"] == id:
            return word
    return None

def json2_print(data: dict):

    print(json.dumps(data, indent=4,  ensure_ascii=False))


if __name__ == "__main__":

    test = JPN_Dictionary("dict/jmdict-eng-3.6.1.json")

    # with open("dict/jmdict-eng-3.6.1.json", encoding="utf-8") as file:
        # data = json.load(file)

    # print(data["version"])

    find_me = '大学'

    test.find_by_word(find_me)
    test.populate_definitions()

    print(test)

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