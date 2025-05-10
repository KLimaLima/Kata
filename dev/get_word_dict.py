import json

with open("dict/jmdict-eng-3.6.1.json", encoding="utf-8") as file:
    data = json.load(file)

print(data["version"])
print(data["words"][0].keys())
print(data["words"][30]["kanji"])
print(data["words"][30]["kana"])
print(data["words"][30]["sense"])