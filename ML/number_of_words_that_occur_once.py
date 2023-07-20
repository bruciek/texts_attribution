def number_of_words_that_occur_once(words:list[str]) -> int:
    count = 0
    unique_word = set(words)
    for word in unique_word:
        if words.count(word) == 1:
            count += 1
    return count


