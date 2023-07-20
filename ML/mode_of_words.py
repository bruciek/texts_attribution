def mode_of_words(words: list[str]) -> str:
    from collections import defaultdict

    temp = defaultdict(int)
    ma = -1
    dic = {'temp': ''}

    for word in words:
        temp[word] += 1
        if temp[word] > ma:
            ma = temp[word]
            dic['temp'] = word
        elif temp[word] == ma and len(dic['temp']) < len(word):
            dic['temp'] = word

    return dic['temp']
