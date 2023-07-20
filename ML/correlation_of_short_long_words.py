def correlation_of_short_long_words(words:list[str]) -> float:
    long = 0
    short = 0
    for word in words:
        if len(word) < 5:
            short += 1
        elif len(word) > 8:
            long += 1
    return short / long
