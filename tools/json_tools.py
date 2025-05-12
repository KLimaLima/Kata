import json

def json2_print(data: dict):

    print(json.dumps(data, indent=4,  ensure_ascii=False))

if __name__ == "__main__":

    data = {1: ['university', 'college'], 2: ['former imperial university of Japan (established under the ritsuryō system for the training of government administrators)'], 3: ['the Great Learning (one of the Four Books)']}

    json.dumps(data, indent=4, ensure_ascii=False)