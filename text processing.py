from bs4 import BeautifulSoup as Soup
import chardet
import unicodedata

with open('Данные/Не обработанные/Л. Н. Андреев/andreew_l_n-text_0064.fb2', 'rb') as f:
    rtext = f.read()
    rtext_unicode = rtext.decode(chardet.detect(rtext)["encoding"]).encode("utf8").decode("utf8")
    text = unicodedata.normalize("NFKD", rtext_unicode)
    soup = Soup(text, features="xml")
names = [offer.get_text(strip=True) for offer in soup.find_all('p')]
print(*names, sep='\n')

