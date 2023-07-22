def average_lenght_of_nouns(lemma_part_speech): #средняя длина существительных
    nouns = lemma_part_speech'NOUN']
    count = len(''.join(nouns))
    return count/len(nouns)

def average_lenght_of_adjectives(lemma_part_speech): #средняя длина прилагательных
    adj = lemma_part_speech'ADJ']
    count = len(''.join(adj))
    return count/len(adj)

def average_lenght_of_adverbs(lemma_part_speech): #средняя длина наречий
    adv = lemma_part_speech['ADV']
    count = len(''.join(adv))
    return count/len(adv)

def average_lenght_of_verbs(lemma_part_speech): #средняя длина глаголов
    verbs = lemma_part_speech['VERB']
    count = len(''.join(verbs))
    return count/len(verbs)

def freq_word_from_adjective(lemma_part_speech):
    adjectives = lemma_part_speech['ADJ']
    temp = defaultdict(int)
    for word in adjectives:
        temp[word] += 1
    w = max(temp, key=temp.get)
    return adjectives.count(w) / len(adjectives)


def freq_word_from_noun(lemma_part_speech):
    nouns = lemma_part_speech['NOUN']
    temp = defaultdict(int)
    for word in nouns:
        temp[word] += 1
    w = max(temp, key=temp.get)
    return nouns.count(w) / len(nouns)


def freq_word_from_verbs(lemma_part_speech):
    verbs = lemma_part_speech['VERB']
    temp = defaultdict(int)
    for word in verbs:
        temp[word] += 1
    w = max(temp, key=temp.get)
    return verbs.count(w) / len(verbs)

def freq_word_from_adverbs(lemma_part_speech):
    adverbs = lemma_part_speech['ADV']
    temp = defaultdict(int)
    for word in adverbs:
        temp[word] += 1
    w = max(temp, key=temp.get)
    return adverbs.count(w) / len(adverbs)

def avg_syllable_per_noun(lemma_part_speech) -> float:
    nouns = lemma_part_speech['NOUN']
    vowels = 'аеёиоуыэюя'
    syllable_count = 0
    for noun in nouns:
        for letter in noun:
            if letter in vowels:
                syllable_count += 1
    return syllable_count / len(nouns)

def avg_syllable_per_verb(lemma_part_speech) -> float:
    verbs = lemma_part_speech['VERB']
    vowels = 'аеёиоуыэюя'
    syllable_count = 0
    for verb in verbs:
        for letter in verb:
            if letter in vowels:
                syllable_count += 1
    return syllable_count / len(verbs)

def avg_syllable_per_adjective(lemma_part_speech) -> float:
    adjectives = lemma_part_speech['ADJ']
    vowels = 'аеёиоуыэюя'
    syllable_count = 0
    for adjective in adjectives:
        for letter in adjective:
            if letter in vowels:
                syllable_count += 1
    return syllable_count / len(adjectives)

def avg_syllable_per_adverb(lemma_part_speech) -> float:
    adverbs = lemma_part_speech['ADV']
    vowels = 'аеёиоуыэюя'
    syllable_count = 0
    for adverb in adverbs:
        for letter in adverb:
            if letter in vowels:
                syllable_count += 1
    return syllable_count / len(adverbs)


def get_feature_lemma_part_speech(doc):
    lemma_part_speech = get_lemma_part_speech(doc)
    func_lemma_part_speech = [avg_syllable_per_adverb, avg_syllable_per_adjective, avg_syllable_per_verb, avg_syllable_per_noun, freq_word_from_adverbs, freq_word_from_verbs, freq_word_from_adverbs, freq_word_from_noun, average_lenght_of_verbs, average_lenght_of_adverbs, average_lenght_of_adjectives, average_lenght_of_nouns]
    lemma_part_speech_list = [func(lemma_part_speech) for func in func_lemma_part_speech]
    return lemma_part_speech_list