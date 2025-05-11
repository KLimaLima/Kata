import MeCab

def tokenize_jpn(text):

    wakati = MeCab.Tagger("-Owakati")

    list_words = wakati.parse(text).split()

    return list_words

if __name__ == "__main__":

    wakati = MeCab.Tagger("-Owakati")

    sentence2 = "もう少し選択肢が広がるかと思います"
    sentence = "先生とお弁当のおかずを 交換していた ひとりぼっちな子"

    list_words01 = wakati.parse(sentence).split()

    tagger = MeCab.Tagger()

    # list_words02 = tagger.parse(sentence).split()

    print(list_words01)
    # print(list_words02)