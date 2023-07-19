def average_length_of_sentences(sentences:list[str]) -> float:
    sentences_len_sum = 0
    for sentence in sentences:
        sentences_len_sum += len(sentence.replace(' ', ''))

    return sentences_len_sum / len(sentences)

#Пока чисто средняя длина предложений по символам, не считая пробелы
