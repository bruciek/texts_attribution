def correlation_of_short_long_words(doc): #отношение коротких слов к длинным. на вход принимает произведения
    short = 0
    long = 0
    words = get_words(doc)
    for word in words:
        if len(word) < 5:
            short += 1
        elif len(word) > 8:
            long += 1
    return short / long

def correlation_of_long_medium_words(doc):
    long = 0
    medium = 0
    words = get_words(doc)
    for word in words:
        if  4 <= len(word) <= 8:
            medium += 1
        elif len(word) > 8:
            long += 1
    return long / medium
#%%
def semicolon_freq(doc):
    return doc.text.count(';') / len(doc.text)
#%%
def count_upper_words(doc):
    count = 0
    words = get_words(doc)
    for word in words:
        if word.isupper() == True:
            count += 1
    return count
#%%
def freq_of_freq_word(doc):
    temp = defaultdict(int)
    words = get_words(doc)
    for word in words:
        temp[word] += 1
    w = max(temp, key=temp.get)
    return words.count(w)
#%%
def freq_word_from_adjective(doc):
    adjectives = get_lemma_part_speech(doc, 'ADJ')
    temp = defaultdict(int)
    for word in adjectives:
        temp[word] += 1
    w = max(temp, key=temp.get)
    return adjectives.count(w) / len(adjectives)
#%%
def freq_word_from_noun(doc):
    nouns = get_lemma_part_speech(doc, 'NOUN')
    temp = defaultdict(int)
    for word in nouns:
        temp[word] += 1
    w = max(temp, key=temp.get)
    return nouns.count(w) / len(nouns)
#%%
def freq_word_from_verbs(doc):
    verbs = get_lemma_part_speech(doc, 'VERB')
    temp = defaultdict(int)
    for word in verbs:
        temp[word] += 1
    w = max(temp, key=temp.get)
    return verbs.count(w) / len(verbs)