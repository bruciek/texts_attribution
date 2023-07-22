from collections import Counter
def foo(freq_words: Counter) -> float:
 return len(freq_words.keys())

 def frequency_of_a(freq_words: Counter) -> float:
  keys = freq_words['а']
  return keys

def frequency_of_o(freq_words: Counter) -> float:
 keys = freq_words['о']
 return keys

 def frequency_of_e(freq_words: Counter) -> float:
  keys = freq_words['е']
  return keys
def frequency_of_n(freq_words: Counter) -> float:
 keys = freq_words['н']
 return keys

def frequency_of_t(freq_words: Counter) -> float:
  keys = freq_words['т']
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