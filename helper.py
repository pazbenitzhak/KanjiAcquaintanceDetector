import json

def fetch_joyo_list(path):
    with open(path, encoding='utf-8') as f:
        return set(json.load(f))

def is_kanji(char):
    #TODO: complete function
    return

def is_joyo_kanji(kanji, joyo_list):
    if kanji in joyo_list:
        return True
    #TODO: complete function
    return False

