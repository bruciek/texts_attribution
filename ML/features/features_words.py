from collections import Counter


def frequency_of_a(freq_words: Counter) -> float:
    keys = freq_words['а']
    return keys


def frequency_of_longest_word(freq_words: Counter) -> float:
    keys = freq_words.keys()
    longest = freq_words[sorted(keys)[0]]
    return longest / len(keys)


def count_upper_words(freq_words: Counter) -> float:
    keys = freq_words.keys()
    up_count = 0
    for key in keys:
        if key.isupper():
            up_count += freq_words[key]
            return up_count

func_words = [count_upper_words, frequency_of_longest_word, frequency_of_a]
def get_feature_word(doc):
    freq_words = Counter(doc.text)
    words_list = [func(freq_words) for func in func_words]
    return words_list
