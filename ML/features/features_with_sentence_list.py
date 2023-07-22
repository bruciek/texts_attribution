from ML.natasha_func import get_sents


def capitalized_words_count_without_start_of_sentences(sentences):
    alphabet_capitalized = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    count = 0
    for sentence in sentences:
        for i in range(1, len(sentence)):
            letter_prev = sentence[i-1]
            letter_curr = sentence[i]
            if letter_prev == ' ' and letter_curr in alphabet_capitalized:
                count += 1
    return count

def most_common_first_letter_in_sentences(sentences):
    alphabet_capitalized = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    first_letter_occurrences = [0] * len(alphabet_capitalized)
    for sentence in sentences:
        k = 0
        while sentence[k] not in alphabet_capitalized and k<len(sentence)-1: k += 1
        if k != len(sentence) - 1:
            first_letter_occurrences[alphabet_capitalized.index(sentence[k])] += 1
    return alphabet_capitalized.index(alphabet_capitalized[first_letter_occurrences.index(max(first_letter_occurrences))])

def avg_length_of_sentence_by_letters(sentences):
    return len(''.join(sentences).replace(' ', '')) / len(sentences)

FUNC_LIST = [capitalized_words_count_without_start_of_sentences, most_common_first_letter_in_sentences, avg_length_of_sentence_by_letters]
def get_feature_sents(doc):
    sentences = get_sents(doc)
    sent_feature_list = [func(sentences) for func in FUNC_LIST]
    return sent_feature_list