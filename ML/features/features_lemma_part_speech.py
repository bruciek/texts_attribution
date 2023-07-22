def average_lenght_of_nouns(doc): #средняя длина существительных
    nouns = get_lemma_part_speech(doc)['NOUN']
    count = len(''.join(nouns))
    return count/len(nouns)

def average_lenght_of_adjectives(doc): #средняя длина прилагательных
    adj = get_lemma_part_speech(doc)['ADJ']
    count = len(''.join(adj))
    return count/len(adj)

def average_lenght_of_adverbs(doc): #средняя длина наречий
    adv = get_lemma_part_speech(doc)['ADV']
    count = len(''.join(adv))
    return count/len(adv)

def average_lenght_of_verbs(doc): #средняя длина глаголов
    verbs = get_lemma_part_speech(doc)['VERB']
    count = len(''.join(verbs))
    return count/len(verbs)

def freq_word_from_adjective(doc):
    adjectives = get_lemma_part_speech(doc)['ADJ']
    temp = defaultdict(int)
    for word in adjectives:
        temp[word] += 1
    w = max(temp, key=temp.get)
    return adjectives.count(w) / len(adjectives)


def freq_word_from_noun(doc):
    nouns = get_lemma_part_speech(doc)['NOUN']
    temp = defaultdict(int)
    for word in nouns:
        temp[word] += 1
    w = max(temp, key=temp.get)
    return nouns.count(w) / len(nouns)


def freq_word_from_verbs(doc):
    verbs = get_lemma_part_speech(doc)['VERB']
    temp = defaultdict(int)
    for word in verbs:
        temp[word] += 1
    w = max(temp, key=temp.get)
    return verbs.count(w) / len(verbs)

def freq_word_from_adverbs(doc):
    adverbs = get_lemma_part_speech(doc)['ADV']
    temp = defaultdict(int)
    for word in adverbs:
        temp[word] += 1
    w = max(temp, key=temp.get)
    return adverbs.count(w) / len(adverbs)

def avg_syllable_per_noun(doc) -> float:
    nouns = get_lemma_part_speech(doc)['NOUN']
    vowels = 'аеёиоуыэюя'
    syllable_count = 0
    for noun in nouns:
        for letter in noun:
            if letter in vowels:
                syllable_count += 1
    return syllable_count / len(nouns)

def avg_syllable_per_verb(doc) -> float:
    verbs = get_lemma_part_speech(doc) ['VERB']
    vowels = 'аеёиоуыэюя'
    syllable_count = 0
    for verb in verbs:
        for letter in verb:
            if letter in vowels:
                syllable_count += 1
    return syllable_count / len(verbs)

def avg_syllable_per_adjective(doc) -> float:
    adjectives = get_lemma_part_speech(doc) ['ADJ']
    vowels = 'аеёиоуыэюя'
    syllable_count = 0
    for adjective in adjectives:
        for letter in adjective:
            if letter in vowels:
                syllable_count += 1
    return syllable_count / len(adjectives)

def avg_syllable_per_adverb(doc) -> float:
    adverbs = get_lemma_part_speech(doc) ['ADV']
    vowels = 'аеёиоуыэюя'
    syllable_count = 0
    for adverb in adverbs:
        for letter in adverb:
            if letter in vowels:
                syllable_count += 1
    return syllable_count / len(adverbs)