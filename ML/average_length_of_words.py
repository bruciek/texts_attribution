def average_length_of_words(words:list[str]) -> float:
    length_sum = 0
    for word in words:
        length_sum += len(word)

    return length_sum / len(words)
