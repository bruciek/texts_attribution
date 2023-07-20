def average_number_of_syllables(words:list[str]) -> float:
    syllables_count = 0
    vowels = 'аеёиоуыэюя'
    for word in words:
        for vowel in vowels:
            syllables_count += word.count(vowel)    #(CLOWN EMOJI)

    return syllables_count / len(words)
