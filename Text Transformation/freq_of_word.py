#функция на частоту союзов, предлогов, частиц
def freq_of_word(all_words, words_for_freq) -> float:
    count = 0
    for word in all_words:
        if word in words_for_freq:
            count += 1
    return count / len(all_words)