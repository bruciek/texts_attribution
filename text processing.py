from bs4 import BeautifulSoup as Soup
import chardet
import unicodedata
import re

with open('Данные/Не обработанные/А. И. Герцен/gercen_a_i-text_0010.fb2', 'rb') as f:
    rtext = f.read()
    rtext_unicode = rtext.decode(chardet.detect(rtext)["encoding"]).encode("utf8").decode("utf8")
    text = unicodedata.normalize("NFKD", rtext_unicode)
    soup = Soup(text[text.find('<body>'):], features="xml")

without_strong = []
for offer in soup.find_all('p'):
    if '<strong>' not in str(offer) and '<emphasis>' not in str(offer):
        without_strong.append(offer.get_text(strip=True))
names = ' '.join(without_strong[2:])

# текст в предложения
def to_sentences(names):
    end_signs = '.!?;'
    for sign in end_signs:
        names = names.replace(sign, '*')
    sentences = names.split('*')
    only_russian_sentences = []
    for sentence in sentences:
        only_russian_sentences.append(re.sub("[^а-яА-Я,:]", " ", str(sentence)))
    return only_russian_sentences

# текст в слова
def to_word(names):
     names_russian = re.sub("[^а-яА-Я]", " ", str(names)).split(" ")
     words = []
     for name in names_russian:
         if name != '': words.append(name)
     return words

print(to_sentences(names))

