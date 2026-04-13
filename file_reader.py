from helper import is_joyo_kanji
from helper import is_kanji

def read_from_files(txt_files_path, csv_files,joyo_list):
    total_kanji_set, joyo_kanji_set = set(), set() 
    for txt_file_path in txt_files_path:
        with open(txt_file_path, "r", encoding='utf-8') as f:
            text = f.read()
        for ch in text:
            if is_kanji(ch):
                total_kanji_set.add(ch)
                if is_joyo_kanji(ch):
                    joyo_kanji_set.add(ch)
                    
    return