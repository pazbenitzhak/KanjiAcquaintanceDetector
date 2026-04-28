import json
import regex

kanji_pattern = regex.compile(r'\p{Han}')

def fetch_joyo_list(path):
    with open(path, encoding='utf-8') as f:
        return set(json.load(f))

def is_kanji(char):
    return bool(kanji_pattern.search(char))

def is_joyo_kanji(kanji, joyo_list):
    if kanji in joyo_list:
        return True
    return False

