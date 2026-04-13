import json

def fetch_joyo_list(path):
    with open(path, encoding='utf-8') as f:
        return set(json.load(f))

def is_kanji(char):
    return

def is_joyo_kanji(kanji, joyo_list):
    return

