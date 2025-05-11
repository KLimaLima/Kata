import json
import time

class JPN_Dictionary:

    loaded_dict = False
    
    version = None
    words = None
    
    def __init__(self, dict_file):

        if self.loaded_dict:
            return
        # TODO: what if wants to use another dict file
            
        with open(dict_file, encoding="utf-8") as file:
            data = json.load(file)
        
        self.loaded_dict = True

        self.version = data["version"]

        self.words = data["words"]
        
    def find_by_word(self, find_me):

        for word in self.words:

            for var in word["kanji"]:

                if find_me == var["text"]:

                    return word
        
        return None

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

    with open("dict/jmdict-eng-3.6.1.json", encoding="utf-8") as file:
        data = json.load(file)

    print(data["version"])

    find_me = '大学'

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

    start_time = time.time()

    print(find_by_word(find_me))

    end_time = time.time()
    print(end_time - start_time)

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