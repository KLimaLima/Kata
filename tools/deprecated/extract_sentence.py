# REASON OF DEPRECATION
# - using nagisa which is slow
# - in favor of using MeCab (the more offical-ish jpn tokenizer and much faster)

import nagisa

def extract_sentence(file_path):
    """Extracts the words inside of a sentence

    :param file_path: absolute path of the file
    :return: list[list[words]]
    """

    with open(file_path, 'r', encoding='utf-8') as rf:

        contents = rf.readlines()

        for content in contents:

            for word in nagisa.tagging(content).words:
                print(word)

if __name__ == "__main__":
    
    file = 'subs_of_Bocchi the Rock! - S01E01 - Lonely Rolling Bocchi HDTV-1080p.ja.srt.txt'

    with open(f'out/{file}', 'r', encoding= 'utf-8') as rf:

        contents = rf.readlines()

        count = 0

        for content in contents:

            count += 1

            if count >= 30:
                break

            print(nagisa.tagging(content).words)

            # for word in nagisa.tagging(content).words:
            #     print(word)