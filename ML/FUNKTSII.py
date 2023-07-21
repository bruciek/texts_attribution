def frequency_of_i(book): #частоты союза и (легенда)
    from natasha_func import get_words
    count = 0
    words = get_words(book)
    for word in words:
        if word == 'и':
            count += 1
    return count / len(words)
#%%
def frequency_of_comma(book): #частоты запятых
    symbol_count = book.count(',')
    return symbol_count / len(book)

#%%
def frequency_of_dot(book): #частоты точек
        symbol_count = book.count('.')
        return symbol_count / len(book)
#%%
def frequency_of_exclamation_mark(book): #частоты восклицательных знаков
    symbol_count = book.count('!')
    return symbol_count / len(book)
#%%
def frequency_of_question_mark(book): #частоты вопросительных знаков
    symbol_count = book.count('?')
    return symbol_count / len(book)
#%%
def frequency_of_brackets(book): #частоты скобок
    symbol_count = book.count('(') + book.count(')') + book.count('[') + book.count(']')
    return symbol_count / len(book)

#%%
def frequency_of_quotation_marks(book): #частоты кавычек
    symbol_count = book.count('"') + book.count('«') +  book.count('»')
    return symbol_count / len(book)

#%%
def frequency_of_numbers(book): #частоты циферов
    symbol_count = 0
    number = '0123456789'
    for num in number:
        symbol_count += book.count(number)
    return symbol_count / len(book)
#%%
def number_of_unique_words(book): #количество уникальных слов
    from natasha_func import get_lemma_words
    words = get_lemma_words(book)
    return len(set(words))
#%%
def number_of_words_that_occur_once(book): #количество слов, появляющихся единожды
    from natasha_func import get_lemma_words
    words = get_lemma_words(book)
    count = 0
    unique_word = set(words)
    for word in unique_word:
        if words.count(word) == 1:
            count += 1
    return count
#%%
def frequency_of_longest_word(book): #частота самого длинного слова
    from natasha_func import get_lemma_words
    words = sorted(get_lemma_words(book), key = len)
    longest = words[-1]
    return words.count(longest) / len(words)
#%%
def average_lenght_of_sentence_by_letters(book): #средняя длина предложений по буквам
    from natasha_func import get_sents
    sents = get_sents(book)
    sum_len = sum([len(sent) for sent in sents])
    return sum_len/ len(sents)
#%%
def frequency_of_words_in_initial_form(book): #частота слов в начальной форме
    from natasha_func import get_words
    from natasha_func import get_lemma_words
    words = get_words(book)
    lemma_words = get_lemma_words(book)
    count = 0
    for i in range(len(words)):
        if words[i] == lemma_words[i]: count += 1
    return count / len(words)

def correlation_of_vowels_consonants(book):#отношение согласных букв к гласным
    consonants = 0
    c = 'уеыаоэяиёю'
    vowels = 0
    v = 'йцкнгшщзхфвпрлджчсмтб'
    for glas in c: consonants += book.count(glas)
    for soglas in v: vowels += book.count(soglas)
    return glas/soglas

def most_common_first_letter_in_words(book): #самая частая первая буква в словах
    from natasha_func import get_words
    words = get_words(book.lower())
    first_letters = ""
    for word in words:
        first_letters += word[0]
    alf = 'цукенгшщзхъфывапролджэячсмитьбю'
    freq = [0] * len(alf)
    for i in range(len(alf)):
        freq[i] += first_letters.count(alf[i])
    return alf.index(max(freq))

def most_common_first_letter_in_sents(book): #самая частая первая буква в предложениях
    from natasha_func import get_sents
    sents = get_sents(book.lower())
    first_letters = ""
    for sent in sents:
            first_letters += sent[0]
    alf = 'цукенгшщзхъфывапролджэячсмитьбю'
    freq = [0] * len(alf)
    for i in range(len(alf)):
        freq[i] += first_letters.count(alf[i])
    return alf.index(max(freq))
#%%
def frequency_of_a(book): #частоты букв а
    symbol_count = book.count('а')
    return symbol_count / len(book)

#%%
def frequency_of_o(book): #частоты букв о
    symbol_count = book.count('о')
    return symbol_count / len(book)
#%%
def frequency_of_е(book): #частоты букв e
    symbol_count = book.count('e')
    return symbol_count / len(book)

#%%
def frequency_of_n(book): #частоты букв н
    symbol_count = book.count('н')
    return symbol_count / len(book)
#%%
def frequency_of_t(book): #частоты букв т
    symbol_count = book.count('т')
    return symbol_count / len(book)

def average_length_of_help_words(book): #средняя длина служебных слов
    help_words = 'и в не на что с а как это по к но у из за от о так для же все или бы если до то да при нет чтобы даже ни раз ну со под много ли чем надо без через об конечно ведь хотя перед между лишь уж над однако право вообще например правда про оно кроме будто среди значит действительно из-за хоть все-таки наконец против наверное ко пусть словно поскольку впрочем либо главное вроде пол ж было разве чтоб вместо никак спасибо зато видимо кажется ибо лучше б пожалуйста ради сквозь мимо наоборот во-первых мол кино собственно благодаря пост пожалуй есть из-под тем неужели случайно ой напротив вероятно во-вторых спустя себе помимо путем вне плюс обо наверно э насчет включая наверняка мм безусловно увы следовательно де благо якобы верно ага ох по-видимому несомненно вернее толк изо таки эх че словом нежели дескать эй вопреки вице вследствие минус стук передо ан аж угу марш пускай дабы ай посредством ха меж бывало небось ы ну-ка в-третьих ура коли ввиду единственно ха-ха поди ежели гамма притом тьфу алло се топ коль ю ишь близ скрип дак то-то сверх безо пред бум неужто ух ей-богу видео ого ку воистину авто ль ото фу наподобие му иль ну-ну этак хм бишь авось оп невесть бесспорно пас аминь уф эдак гм ба чик браво кабы яко средь подо пардон ава вишь в-четвертых нате постольку превыше тик ниче ака слышь тюк бис хе-хе бац исключая ме ау'.split(' ')
    from natasha_func import get_lemma_words
    lenght = 0
    count = 0
    words = get_lemma_words(book)
    for word in words:
        if word in help_words:
            count += 1
            lenght += len(word)
    return lenght/count

def len_of_most_common_word(book): #длина самого частого слова в тексте
    from natasha_func import get_lemma_words
    words = get_lemma_words(book)
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

    chast = dic['temp']
    return len(chast)

def average_lenght_of_nouns(book): #средняя длина существительных
    from natasha_func import get_lemma_part_speech
    nouns = get_lemma_part_speech(book, 'NOUN')
    count = 0
    for noun in nouns:
        count += len(noun)
    return count/len(nouns)

def average_lenght_of_adjectives(book): #средняя длина прилагательных
    from natasha_func import get_lemma_part_speech
    nouns = get_lemma_part_speech(book, 'ADJ')
    count = 0
    for noun in nouns:
        count += len(noun)
    return count/len(nouns)

def average_lenght_of_adverbs(book): #средняя длина наречий
    from natasha_func import get_lemma_part_speech
    nouns = get_lemma_part_speech(book, 'ADV')
    count = 0
    for noun in nouns:
        count += len(noun)
    return count/len(nouns)

def average_lenght_of_verbs(book): #средняя длина глаголов
    from natasha_func import get_lemma_part_speech
    nouns = get_lemma_part_speech(book, 'VERB')
    count = 0
    for noun in nouns:
        count += len(noun)
    return count/len(nouns)


