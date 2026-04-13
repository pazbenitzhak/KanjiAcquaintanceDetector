from file_reader import read_from_files 
from url_reader import read_from_urls
from helper import fetch_joyo_list

joyo_list_path = "data/kanji-jouyou.json"
joyo_list = fetch_joyo_list(joyo_list_path)

def main(txt_files, csv_files, urls):
    files_total_kanji, files_joyo_kanji = read_from_files(txt_files,csv_files,joyo_list)
    urls_total_kanji, url_joyo_kanji = read_from_urls(urls,joyo_list)

    total_kanji_union = files_total_kanji | urls_total_kanji
    joyo_kanji_union = files_joyo_kanji | url_joyo_kanji

    print(f"you are acquainted with {len(total_kanji_union)} distinct kanji")
    print(f"you are acquainted with {len(joyo_kanji_union)} distinct joyo kanji, "
          f", out of {len(joyo_list)} such kanji")
    return