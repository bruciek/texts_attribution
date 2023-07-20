#from natasha import *
def average_length_of_sentences(sentences:list[str], len_by_words:bool) -> float:
    sentences_len_sum = 0

    if len_by_words:
        segmenter = Segmenter()
        doc = Doc(''.join(sentences))
        doc.segment(segmenter)
        only_words = []
        for token in doc.tokens:
            only_words.append(token)
        return len(only_words) / len(sentences)

    for sentence in sentences:
        sentences_len_sum += len(sentence.replace(' ', ''))
    return sentences_len_sum / len(sentences)
