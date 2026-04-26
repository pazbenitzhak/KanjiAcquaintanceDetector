from helper import is_joyo_kanji
from helper import is_kanji
import pandas as pd


def read_text_files(txt_files_path,joyo_list):
    total_kanji_set, joyo_kanji_set = set(), set() 
    for txt_file_path in txt_files_path:
        with open(txt_file_path, "r", encoding='utf-8') as f:
            text = f.read()
            for ch in text:
                if is_kanji(ch):
                    total_kanji_set.add(ch)
                    if is_joyo_kanji(ch,joyo_list):
                        joyo_kanji_set.add(ch)

    return total_kanji_set, joyo_kanji_set

def read_csv_files(csv_files_path,joyo_list):
    total_kanji_set, joyo_kanji_set = set(), set() 
    for csv_file_path in csv_files_path:
        csv_file = pd.read_csv(csv_file_path, encoding='utf-8-sig')
        #TODO: complete function

    return total_kanji_set, joyo_kanji_set

def read_from_files(txt_files_path, csv_files_path,joyo_list):
    total_txt_kanji, txt_joyo_kanji = read_text_files(txt_files_path,joyo_list)
    total_csv_kanji, txt_csv_kanji = read_csv_files(csv_files_path,joyo_list)

    total_kanji_set = total_txt_kanji | total_csv_kanji
    joyo_kanji_set = txt_csv_kanji | txt_joyo_kanji
                    
    return total_kanji_set, joyo_kanji_set