from helper import is_joyo_kanji, is_kanji
import re
import requests
from bs4 import BeautifulSoup


valid_iknow_pattern = re.compile(r"(https?://)?(www\.)?iknow\.jp/courses/\d{6}")

def is_valid_iknow_url(url):
    return valid_iknow_pattern.fullmatch(url) is not None

def extract_page_id_from_url(url):
    match = re.search(r'(\d+)$',url)
    return match.group(1)

def read_from_iknow(url,joyo_list):
    iknow_total_vocab_kanji, iknow_joyo_vocab_kanji = set(), set()
    page_id = extract_page_id_from_url(url)
    url_for_request = f"https://iknow.jp/api/v2/goals/{page_id}"
    try:
        response = requests.get(url_for_request,timeout=5)

        if response.status_code==200: #success:
            data = response.json()
            vocab = [entry["item"]["cue"]["text"] for entry in data["goal_items"]]
            for word in vocab:
                for letter in word:
                    if is_kanji(letter):
                        iknow_total_vocab_kanji.add(letter)
                        if is_joyo_kanji(letter,joyo_list):
                            iknow_joyo_vocab_kanji.add(letter)
            return response.status_code, iknow_total_vocab_kanji, iknow_joyo_vocab_kanji
            
        elif 400<=response.status_code<500:
            print(f"Client error {response.status_code} for address {url}")
        
        elif 500<=response.status_code<600:
            print(f"Server error {response.status_code} for {url}")
    
    except requests.exceptions.RequestException as e:
        print(f"Request failed for {url}: {e}")
    
    return None, iknow_total_vocab_kanji, iknow_joyo_vocab_kanji
    


def read_gen_scrap(url,joyo_list):
    page_total_vocab_kanji, page_joyo_vocab_kanji = set(), set()
    try:
        response = requests.get(url,timeout=5)
        if response.status_code==200: #success:
            soup = BeautifulSoup(response.text,"html.parser")
            text = soup.get_text()
            for letter in text:
                if is_kanji(letter):
                    page_total_vocab_kanji.add(letter)
                    if is_joyo_kanji(letter,joyo_list):
                        page_joyo_vocab_kanji.add(letter)
            return response.status_code, page_total_vocab_kanji, page_joyo_vocab_kanji
            
        elif 400<=response.status_code<500:
            print(f"Client error {response.status_code} for address {url}")
        
        elif 500<=response.status_code<600:
            print(f"Server error {response.status_code} for {url}")
    
    except requests.exceptions.RequestException as e:
        print(f"Request failed for {url}: {e}")
    return None, page_total_vocab_kanji, page_joyo_vocab_kanji


def read_from_urls(urls,joyo_list):
    iknow_total_kanji, iknow_joyo_kanji = set(), set()
    others_total_kanji, others_joyo_kanji = set(), set()
    for url in urls:
        if is_valid_iknow_url(url):
            resp,url_total_kanji, url_joyo_kanji = read_from_iknow(url,joyo_list)
            if resp:
                iknow_total_kanji |= url_total_kanji
                iknow_joyo_kanji |= url_joyo_kanji
        else:
            resp, url_total_kanji, url_joyo_kanji = read_gen_scrap(url,joyo_list)
            if resp:
                others_total_kanji |= url_total_kanji
                others_joyo_kanji |= url_joyo_kanji
    return iknow_total_kanji, iknow_joyo_kanji, others_total_kanji, others_joyo_kanji