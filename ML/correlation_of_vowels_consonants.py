def correlation_of_vowels_consonants(text: str) -> float:
    consonants = 0
    c = 'уеыаоэяиёю'
    vowels = 0
    v = 'йцкнгшщзхфвпрлджчсмтб'
    text = text.replace(' ', '')
    for i in text:
        if i in c:
            consonants += 1
        elif i in v:
            vowels += 1
    return consonants / vowels



