import nagisa

file = 'subs_of_Bocchi the Rock! - S01E01 - Lonely Rolling Bocchi HDTV-1080p.ja.srt.txt'

with open(f'out/{file}', 'r', encoding= 'utf-8') as rf:

    contents = rf.readlines()

    for content in contents:

        for word in nagisa.tagging(content).words:
            print(word)