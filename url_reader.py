from helper import is_joyo_kanji
import re

valid_iknow_pattern = re.compile(r"(https?://)?(www\.)?iknow\.jp/courses/\d{6}")


def read_from_iknow(url,joyo_list):

    #TODO: implement function
    return

def is_valid_iknow_url(url):
    return valid_iknow_pattern.fullmatch(url) is not None

def read_gen_scrap(url,joyo_list):
    #TODO: implement function
    return

def read_from_urls(urls,joyo_list):
    iknow_total_kanji, iknow_joyo_kanji = set(), set()
    others_total_kanji, others_joyo_kanji = set(), set()
    #TODO: complete function
    for url in urls:
        if is_valid_iknow_url(url):
            url_total_kanji, url_joyo_kanji = read_from_iknow(url,joyo_list)
            iknow_total_kanji |= url_total_kanji
            iknow_joyo_kanji |= url_joyo_kanji
        else:
            url_total_kanji, url_joyo_kanji = read_gen_scrap(url,joyo_list)
            others_total_kanji |= url_total_kanji
            others_joyo_kanji |= url_joyo_kanji
    return iknow_total_kanji, iknow_joyo_kanji, others_total_kanji, others_joyo_kanji