import unicodedata

import chardet
from bs4 import BeautifulSoup
from natasha import Segmenter, Doc
import re


def has_cyrillic(text):
    return bool(re.search('[а-яА-Я]', text))


# функция принимает ссылку/путь к тексту и вынимает его из пэшек (написала Маша)
def get_raw_text(path_to_file):
    with open(path_to_file, 'rb') as f:
        rtext = f.read()
        rtext_unicode = rtext.decode(chardet.detect(rtext)["encoding"]).encode("utf8").decode("utf8")
        text = unicodedata.normalize("NFKD", rtext_unicode)
        soup = BeautifulSoup(text[text.find('<body>'):], features="lxml")

    without_strong = []
    for offer in soup.find_all('p'):
        if '<strong>' not in str(offer) and '<emphasis>' not in str(offer):
            without_strong.append(offer.get_text(strip=True))
    text = ' '.join(without_strong[2:])
    return text


# функция принимает текст (тот, что освобожден от пэшек) и выводит список слов (без знаков припенания)
def get_words(text):
    segmenter = Segmenter()
    doc = Doc(text)
    doc.segment(segmenter)
    only_words = []
    for token in doc.tokens:
        if has_cyrillic(token.text):
            only_words.append(token.text)
    return only_words
print(get_words)
