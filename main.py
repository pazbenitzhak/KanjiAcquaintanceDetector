from file_reader import read_from_files 
from url_reader import read_from_urls
from helper import fetch_joyo_list

joyo_list_path = "data/kanji-jouyou.json"
joyo_list = fetch_joyo_list(joyo_list_path)

def main(txt_files, csv_files, urls):
    #TODO: files conversion? doc -> txt, excel (all types) -> csv
    files_total_kanji, files_joyo_kanji = read_from_files(txt_files,csv_files,joyo_list)
    urls_total_kanji, url_joyo_kanji, scrapped_total_kanji, scrapped_joyo_kanji = read_from_urls(urls,joyo_list)

    total_kanji_union = files_total_kanji | urls_total_kanji
    joyo_kanji_union = files_joyo_kanji | url_joyo_kanji

    print(f"you are acquainted with {len(total_kanji_union)} distinct kanji")
    print(f"you are acquainted with {len(joyo_kanji_union)} distinct joyo kanji, "
          f", out of {len(joyo_list)} such kanji")
    
    scrapped_total_addition = scrapped_total_kanji - (scrapped_total_kanji & total_kanji_union)
    scrapped_joyo_addition = scrapped_joyo_kanji - (scrapped_joyo_kanji & joyo_kanji_union)
    
    print(f"scrapped webpages distinct kanji are {len(scrapped_total_kanji)} in number,\
          and could add you {scrapped_total_addition} to the list of distinct acquainted kanji")
    
    print(f"scrapped webpages distinct joyo kanji are {len(scrapped_joyo_kanji)} in number,\
                    and could add you {scrapped_joyo_addition} to list of distinct acquainted joyo kanji")

    return