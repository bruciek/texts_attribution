from natasha import (
    Segmenter,
    MorphVocab,

    NewsEmbedding,
    NewsMorphTagger,

    Doc
)
import json
import markup

from bs4 import BeautifulSoup as Soup
import chardet
import unicodedata
import re

def get_raw_text(path_to_file):
    with open(path_to_file, 'rb') as f:
        rtext = f.read()
        rtext_unicode = rtext.decode(chardet.detect(rtext)["encoding"]).encode("utf8").decode("utf8")
        text = unicodedata.normalize("NFKD", rtext_unicode)
        soup = Soup(text[text.find('<body>'):], features="lxml")

    without_strong = []
    for offer in soup.find_all('p'):
        if '<strong>' not in str(offer) and '<emphasis>' not in str(offer):
            without_strong.append(offer.get_text(strip=True))
    text = ' '.join(without_strong[2:])
    return text

#%%
#%%
def get_doc(text):
    doc = Doc(text)

    segmenter = Segmenter()
    doc.segment(segmenter)

    emb = NewsEmbedding()
    tagger = NewsMorphTagger(emb)
    doc.tag_morph(tagger)

    morph_vocab = MorphVocab()
    for token in doc.tokens:
        token.lemmatize(morph_vocab)
    return doc

def get_only_doc(text):
    doc = Doc(text)
    return doc
#%%
# функция get_doc от get_raw достает doc-и для других функицй
#%%
#%%
import re
def has_cyrillic(text):
    return bool(re.search('[а-яА-Я]', text))


def get_sents(doc):
    sents_list = []
    for sent in doc.sents:
        sents_list.append(sent.text)

    return sents_list

def get_words(doc):
    only_words = []
    for token in doc.tokens:
        if has_cyrillic(token.text):
            only_words.append(token.text)
    return only_words

def get_lemma_words(doc):
    #lemma_words = {_.text: _.lemma for _ in doc.tokens}
    lemma_words = [token.lemma for token in doc.tokens]
    return lemma_words

def get_part_speech(doc, pos):
    part_speech = []
    for token in doc.tokens:
        if token.pos == pos:
            part_speech.append(token.text)
    return part_speech

def get_lemma_part_speech(doc):
    lemma_part_speech = {}
    for token in doc.tokens:
        if token.pos not in lemma_part_speech.keys():
            lemma_part_speech[token.pos] = []
        else:
            lemma_part_speech[token.pos].append(token.lemma)
    return lemma_part_speech
