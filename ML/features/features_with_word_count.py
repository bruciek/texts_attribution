from ML.utils.extended_counter import ExtendedCounter as Counter


def freq_of_dot(freq_chars: Counter) -> float:
    return freq_chars['.'] / freq_chars.total()


def freq_of_comma(freq_chars: Counter) -> float:
    return freq_chars[','] / freq_chars.total()


def freq_of_question_mark(freq_chars: Counter) -> float:
    return freq_chars['!'] / freq_chars.total()


def freq_of_exclamation_mark(freq_chars: Counter) -> float:
    return freq_chars['?'] / freq_chars.total()


def freq_of_bracket(freq_chars: Counter) -> float:
    return (freq_chars['('] + freq_chars[')'] + freq_chars['['] + freq_chars[']']) / freq_chars.total()


def freq_of_quotation(freq_chars: Counter) -> float:
    return (freq_chars['"'] + freq_chars['«'] + freq_chars['»']) / freq_chars.total()


def freq_of_number(freq_chars: Counter) -> float:
    number_counter = 0
    for key in '0123456789':
        number_counter += freq_chars[key]
    return number_counter / freq_chars.total()


def correlation_of_vowels_consonants(freq_chars: Counter) -> float:
    consonant_counter = 0
    for consonant in 'йцкнгшщзхфвпрлджчсмтб':
        consonant_counter += freq_chars[consonant]
    vowels_counter = 0
    for vowel in 'уеыаоэяиёю':
        vowels_counter += freq_chars[vowel]
    return vowels_counter / consonant_counter


def freq_of_semicolon(freq_chars: Counter) -> float:
    return freq_chars[';'] / freq_chars.total()


def freq_of_enter(freq_chars: Counter) -> float:
    return freq_chars[' '] / freq_chars.total()


def freq_of_i(freq_chars: Counter) -> float:
    return freq_chars['и'] / freq_chars.total()


def freq_of_a(freq_chars: Counter) -> float:
    return freq_chars['а'] / freq_chars.total()


def freq_of_o(freq_chars: Counter) -> float:
    return freq_chars['о'] / freq_chars.total()


def freq_of_e(freq_chars: Counter) -> float:
    return freq_chars['е'] / freq_chars.total()


def freq_of_n(freq_chars: Counter) -> float:
    return freq_chars['н'] / freq_chars.total()


def freq_of_t(freq_chars: Counter) -> float:
    return freq_chars['т'] / freq_chars.total()
