import MeCab

wakati = MeCab.Tagger("-Owakati")

sentence = "もらいながら聞いてもらえたらと思います それでは早速1つ目pyonの環境準備に"

list_words01 = wakati.parse(sentence).split()

tagger = MeCab.Tagger()

list_words02 = tagger.parse(sentence)

print(list_words01)
print(list_words02)