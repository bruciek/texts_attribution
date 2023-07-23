def avg_of_binary_sum(bit_array):
    bit_sum = 0
    for i in bit_array:
        bit_sum += int(i)
    return bit_sum / len(bit_array)

def ones_to_zeros(bit_array):
    return bit_array.count('1') / bit_array.count('0')

def zero_count_minus_one_count(bit_array):
    return bit_array.count('0') - bit_array.count('1')

func_bin = [avg_of_binary_sum, ones_to_zeros, zero_count_minus_one_count]
def get_feature_bin(doc):
    text = doc.text
    bit_array = ''.join(format(ord(x), '08b') for x in text)
    bin_features = [func(bit_array) for func in func_bin]
    return bin_features
