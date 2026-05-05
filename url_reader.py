from helper import is_joyo_kanji
import re
import requests

valid_iknow_pattern = re.compile(r"(https?://)?(www\.)?iknow\.jp/courses/\d{6}")

def extract_page_id_from_url(url):
    match = re.search(r'(\d+)$',url)
    return match.group(1)

def read_from_iknow(url,joyo_list):
    iknow_total_vocab_kanji, iknow_joyo_vocab_kanji = set(), set()
    page_id = extract_page_id_from_url(url)
    url_for_request = f"https://iknow.jp/api/v2/goals/{page_id}"
    response = requests.get(url_for_request)
    #TODO: handle wrong status
    data = response.json()
    #key of get request: https://iknow.jp/api/v2/goals/566921?
    #fetch data by http request
    #take all words under vocabulary
    #apply is kanji and gather kanji
    #apply is joyo and gather is joyo
    #TODO: implement function
    return iknow_total_vocab_kanji, iknow_joyo_vocab_kanji

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