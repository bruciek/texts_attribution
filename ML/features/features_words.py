from collections import Counter
from typing import Callable

from natasha import Doc
from functools import wraps


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


special_words = 'в на с за к по из у от для во без до о через со при про' \
                    ' об ко над из-за из-под под и что но а да хотя когда чтобы ' \
                    'если тоже или зато будто не как же ж даже бы ли только вот то' \
                    'ни лишь ведь вон нибудь уже либо'.split()


func_words = [count_upper_words, frequency_of_longest_word, frequency_of_a]
def get_feature_word(doc):
    freq_words = Counter(doc.text)
    words_list = [func(freq_words) for func in func_words]
    return words_list
