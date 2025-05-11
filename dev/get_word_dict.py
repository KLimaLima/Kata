import json

def json2_print(data: dict):

    print(json.dumps(data, indent=4,  ensure_ascii=False))

if __name__ == "__main__":

    with open("dict/jmdict-eng-3.6.1.json", encoding="utf-8") as file:
        data = json.load(file)

    print(data["version"])

    words = data["words"]

    print(words[0].keys())
    print(type(words[30]))
    print(words[30]["kanji"])

    json2_print(words[30])

    print(type(words[30]["kanji"]))
    print(type(words[30]["kana"]))
    print(type(words[30]["sense"]))
    print(len(words[30]["kanji"]))

    print(words[100]["kanji"])
    print(words[100]["kana"])
    print(words[100]["sense"][0])
    json2_print(words[100])

    json2_print(words[150])