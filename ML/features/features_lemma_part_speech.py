from collections import defaultdict

from ML.natasha_func import get_lemma_part_speech


def average_lenght_of_nouns(lemma_part_speech): #средняя длина существительных
    nouns = lemma_part_speech['NOUN']
    count = len(''.join(nouns))
    if len(nouns) != 0:
        return count/len(nouns)
    else: return 0

def average_lenght_of_adjectives(lemma_part_speech): #средняя длина прилагательных
    adj = lemma_part_speech['ADJ']
    count = len(''.join(adj))
    if len(adj) != 0:
        return count/len(adj)
    else:
        return 0
def average_lenght_of_adverbs(lemma_part_speech): #средняя длина наречий
    if 'ADV' in lemma_part_speech.keys():
        adv = lemma_part_speech['ADV']
        count = len(''.join(adv))
        if len(adv) != 0:
            return count/len(adv)
        else:
            return 0
    else: return 0
def average_lenght_of_verbs(lemma_part_speech): #средняя длина глаголов
    verbs = lemma_part_speech['VERB']
    count = len(''.join(verbs))
    if len(verbs) != 0:
        return count/len(verbs)
    else:
        return 0
def freq_word_from_adjective(lemma_part_speech):
    adjectives = lemma_part_speech['ADJ']
    temp = defaultdict(int)
    for word in adjectives:
        temp[word] += 1
    if len(temp) != 0:
        w = max(temp, key=temp.get)
    else: return 0
    if len(adjectives) != 0:
        return adjectives.count(w) / len(adjectives)
    else:
        return 0

def freq_word_from_noun(lemma_part_speech):
    nouns = lemma_part_speech['NOUN']
    temp = defaultdict(int)
    for word in nouns:
        temp[word] += 1
    if len(temp)  != 0:
        w = max(temp, key=temp.get)
    else: return 0
    if len(nouns) != 0:
        return nouns.count(w) / len(nouns)
    else:
        return 0

def freq_word_from_verbs(lemma_part_speech):
    verbs = lemma_part_speech['VERB']
    temp = defaultdict(int)
    for word in verbs:
        temp[word] += 1
    if len(temp)  != 0:
        w = max(temp, key=temp.get)
    else: return 0
    if len(verbs) != 0:
        return verbs.count(w) / len(verbs)
    else:
        return 0
def freq_word_from_adverbs(lemma_part_speech):
    if 'ADV' in lemma_part_speech.keys():
        adverbs = lemma_part_speech['ADV']
        temp = defaultdict(int)
        for word in adverbs:
            temp[word] += 1
        if len(temp)  != 0:
            w = max(temp, key=temp.get)
        else: return 0
        if len(adverbs) != 0:
            return adverbs.count(w) / len(adverbs)
        else:
            return 0
    else: return 0
def avg_syllable_per_noun(lemma_part_speech) -> float:
    nouns = lemma_part_speech['NOUN']
    vowels = 'аеёиоуыэюя'
    syllable_count = 0
    for noun in nouns:
        for letter in noun:
            if letter in vowels:
                syllable_count += 1
    if len(nouns) != 0:
        return syllable_count / len(nouns)
    else:
        return 0
def avg_syllable_per_verb(lemma_part_speech) -> float:
    verbs = lemma_part_speech['VERB']
    vowels = 'аеёиоуыэюя'
    syllable_count = 0
    for verb in verbs:
        for letter in verb:
            if letter in vowels:
                syllable_count += 1
    if len(verbs) != 0:
        return syllable_count / len(verbs)
    else:
        return 0
def avg_syllable_per_adjective(lemma_part_speech) -> float:
    adjectives = lemma_part_speech['ADJ']
    vowels = 'аеёиоуыэюя'
    syllable_count = 0
    for adjective in adjectives:
        for letter in adjective:
            if letter in vowels:
                syllable_count += 1
    if len(adjectives) != 0:
        return syllable_count / len(adjectives)
    else:
        return 0
def avg_syllable_per_adverb(lemma_part_speech) -> float:
    if 'ADV' in lemma_part_speech.keys():
        adverbs = lemma_part_speech['ADV']
        vowels = 'аеёиоуыэюя'
        syllable_count = 0
        for adverb in adverbs:
            for letter in adverb:
                if letter in vowels:
                    syllable_count += 1
        if len(adverbs) != 0:
            return syllable_count / len(adverbs)
        else:
            return 0
    else: return 0
func_lemma_part_speech = [avg_syllable_per_adverb, avg_syllable_per_adjective, avg_syllable_per_verb, avg_syllable_per_noun, freq_word_from_verbs, freq_word_from_adverbs, freq_word_from_noun, freq_word_from_adjective, average_lenght_of_verbs, average_lenght_of_adverbs, average_lenght_of_adjectives, average_lenght_of_nouns]
def get_feature_lemma_part_speech(doc):
    lemma_part_speech = get_lemma_part_speech(doc)

    lemma_part_speech_list = [func(lemma_part_speech) for func in func_lemma_part_speech]
    return lemma_part_speech_list