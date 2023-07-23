def avg_of_binary_sum(text):
    bit_sum = 0
    bit_array = ''.join(format(ord(x), '08b') for x in text)
    for i in bit_array:
        bit_sum += int(i)
    return bit_sum / len(bit_array)

def ones_to_zeros(text):
    bit_array = ''.join(format(ord(x), '08b') for x in text)
    return bit_array.count('1') / bit_array.count('0')

def zero_count_minus_one_count(text):
    bit_array = ''.join(format(ord(x), '08b') for x in text)
    return bit_array.count('0') - bit_array.count('1')

def avg_words_between_commas(text):
    words_count_sum = 0
    words_between = text.split(',')
    for words in words_between:
        words_count_sum += len(words.split(' '))
    return words_count_sum / len(words_between)
