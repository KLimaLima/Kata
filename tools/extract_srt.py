import srt

def extract_srt(file_path, out_path='out/', out_name=None):

    if not out_name:    
        out_name = file_path.split('/')
        out_name = out_name[-1]

    with open(f'res/{file_path}', 'r', encoding= 'utf-8') as rf:

        subs = srt.parse(rf)

        with open(f'{out_path}{out_name}.txt', 'w', encoding='utf-8') as wf:
            
            for sub in subs:

                wf.write(sub.content)
                wf.write('\n\n') # This is to divide it up

if __name__ == "__main__":

    filename = 'Bocchi the Rock! - S01E01 - Lonely Rolling Bocchi HDTV-1080p.ja.srt'
    full_path = ''

    with open(f'res/{filename}', 'r', encoding= 'utf-8') as rf:

        subs = srt.parse(rf)

        # for line in subs:
        #     print(line)

        with open(f'out/subs_of_{filename}.txt', 'w', encoding='utf-8') as wf:
            
            for sub in subs:

                wf.write(sub.content)
                wf.write('\n\n') # This is to divide it up