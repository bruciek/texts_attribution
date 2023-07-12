from bs4 import BeautifulSoup as Soup
import chardet
import unicodedata
import re


with open('Данные/Не обработанные/М. А. Кузмин/kuzmin_m_a-kuzmin1_1.fb2', 'rb') as f:
    rtext = f.read()
    rtext_unicode = rtext.decode(chardet.detect(rtext)["encoding"]).encode("utf8").decode("utf8")
    text = unicodedata.normalize("NFKD", rtext_unicode)
    soup = Soup(text[text.find('<body>'):], features="xml")

without_strong = []
for offer in soup.find_all('p'):
    if '<strong>' not in str(offer) and '<emphasis>' not in str(offer):
        without_strong.append(offer.get_text(strip=True))
names = ' '.join(without_strong[10:])
print(names)

# текст в предложения
# def to_sentences(names):
#     sentences = names.split('.').split('!').split('?')
#     return sentences
# print(to_sentences(names))

# текст в слова
# def to_word(names):
#     names_russian = re.sub("[^а-яА-Я]", " ", str(names)).split(" ")
#     # return(*names_russian, sep='\n')



