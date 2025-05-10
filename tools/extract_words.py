import MeCab

wakati = MeCab.Tagger("-Owakati")

sentence = "もう少し選択肢が広がるかと思います"
sentence2 = "私も"

list_words01 = wakati.parse(sentence).split()

tagger = MeCab.Tagger()

# list_words02 = tagger.parse(sentence).split()

print(list_words01)
# print(list_words02)