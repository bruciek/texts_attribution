from natasha_func import *
from collections import defaultdict

def frequency_of_i(book): #частоты союза и (легенда)
    count = 0
    words = get_words(book)
    for word in words:
        if word == 'и':
            count += 1
    return count / len(words)
#%%
def frequency_of_comma(book): #частоты запятых
    text = book.text
    symbol_count = book.text.count(',')
    return symbol_count / len(text)
#%%
def frequency_of_dot(book): #частоты точек
    text = book.text
    symbol_count = text.count('.')
    return symbol_count / len(text)
#%%
def frequency_of_exclamation_mark(book): #частоты восклицательных знаков
    text = book.text
    symbol_count = text.count('!')
    return symbol_count / len(text)
#%%
def frequency_of_question_mark(book): #частоты вопросительных знаков
    text = book.text
    symbol_count = text.count('?')
    return symbol_count / len(text)
#%%
def frequency_of_brackets(book): #частоты скобок
    text = book.text
    symbol_count = text.count('(') + text.count(')') + text.count('[') + text.count(']')
    return symbol_count / len(text)
#%%
def frequency_of_quotation_marks(book): #частоты кавычек
    text = book.text
    symbol_count = text.count('"') + text.count('«') + text.count('»')
    return symbol_count / len(text)
#%%
def frequency_of_numbers(book): #частоты циферов
    text = book.text
    symbol_count = 0
    number = '0123456789'
    for num in number:
        symbol_count += text.count(num)
    return symbol_count / len(text)
#%%
def number_of_unique_words(book): #количество уникальных слов
    words = get_lemma_words(book)
    return len(set(words))
#%%
def number_of_words_that_occur_once(book): #количество слов, появляющихся единожды
    words = get_lemma_words(book)
    count = 0
    unique_word = set(words)
    for word in unique_word:
        if words.count(word) == 1:
            count += 1
    return count
#%%
def frequency_of_longest_word(book): #частота самого длинного слова
    words = sorted(get_lemma_words(book), key = len)
    longest = words[-1]
    return words.count(longest) / len(words)
#%%
def average_lenght_of_sentence_by_letters(book): #средняя длина предложений по буквам
    sents = get_sents(book)
    sum_len = sum([len(sent) for sent in sents])
    return sum_len / len(sents)
#%%
def frequency_of_words_in_initial_form(book): #частота слов в начальной форме
    words = get_words(book)
    lemma_words = get_lemma_words(book)
    count = 0
    for i in range(len(words)):
        if words[i] == lemma_words[i]: count += 1
    return count / len(words)

def correlation_of_vowels_consonants(book):#отношение согласных букв к гласным
    text = book.text
    consonants = 0
    c = 'уеыаоэяиёю'
    vowels = 0
    v = 'йцкнгшщзхфвпрлджчсмтб'
    for glas in c: consonants += text.count(glas)
    for soglas in v: vowels += text.count(soglas)
    return vowels / consonants

def most_common_first_letter_in_words(book): #самая частая первая буква в словах
    words = get_words(book)
    words = [element.lower() for element in words]
    first_letters = ""
    for word in words:
        first_letters += word[0]
    alf = 'цукенгшщзхъфывапролджэячсмитьбю'
    freq = [0] * len(alf)
    for i in range(len(alf)):
        freq[i] += first_letters.count(alf[i])
    return alf[freq.index(max(freq))]

def most_common_first_letter_in_sents(book): #самая частая первая буква в предложениях
    sents = get_sents(book)
    sents = [element.lower() for element in sents]
    first_letters = ""
    for sent in sents:
            first_letters += sent[0]
    alf = 'цукенгшщзхъфывапролджэячсмитьбю'
    freq = [0] * len(alf)
    for i in range(len(alf)):
        freq[i] += first_letters.count(alf[i])
    return alf[freq.index(max(freq))]
#%%
def frequency_of_a(book): #частоты букв а
    text = book.text
    symbol_count = text.count('а')
    return symbol_count / len(text)

#%%
def frequency_of_o(book): #частоты букв о
    text = book.text
    symbol_count = text.count('о')
    return symbol_count / len(text)
#%%
def frequency_of_е(book): #частоты букв e
    text = book.text
    symbol_count = text.count('e')
    return symbol_count / len(text)

#%%
def frequency_of_n(book): #частоты букв н
    text = book.text
    symbol_count = text.count('н')
    return symbol_count / len(text)
#%%
def frequency_of_t(book): #частоты букв т
    text = book.text
    symbol_count = text.count('т')
    return symbol_count / len(text)

def average_length_of_help_words(book): #средняя длина служебных слов
    help_words = 'и в не на что с а как это по к но у из за от о так для же все или бы если до то да при нет чтобы даже ни раз ну со под много ли чем надо без через об конечно ведь хотя перед между лишь уж над однако право вообще например правда про оно кроме будто среди значит действительно из-за хоть все-таки наконец против наверное ко пусть словно поскольку впрочем либо главное вроде пол ж было разве чтоб вместо никак спасибо зато видимо кажется ибо лучше б пожалуйста ради сквозь мимо наоборот во-первых мол кино собственно благодаря пост пожалуй есть из-под тем неужели случайно ой напротив вероятно во-вторых спустя себе помимо путем вне плюс обо наверно э насчет включая наверняка мм безусловно увы следовательно де благо якобы верно ага ох по-видимому несомненно вернее толк изо таки эх че словом нежели дескать эй вопреки вице вследствие минус стук передо ан аж угу марш пускай дабы ай посредством ха меж бывало небось ы ну-ка в-третьих ура коли ввиду единственно ха-ха поди ежели гамма притом тьфу алло се топ коль ю ишь близ скрип дак то-то сверх безо пред бум неужто ух ей-богу видео ого ку воистину авто ль ото фу наподобие му иль ну-ну этак хм бишь авось оп невесть бесспорно пас аминь уф эдак гм ба чик браво кабы яко средь подо пардон ава вишь в-четвертых нате постольку превыше тик ниче ака слышь тюк бис хе-хе бац исключая ме ау'.split(' ')
    lenght = 0
    count = 0
    words = get_lemma_words(book)
    for word in words:
        if word in help_words:
            count += 1
            lenght += len(word)
    return lenght/count

def len_of_most_common_word(book): #длина самого частого слова в тексте
    words = get_lemma_words(book)

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
    nouns = get_lemma_part_speech(book, 'NOUN')
    count = 0
    for noun in nouns:
        count += len(noun)
    return count/len(nouns)

def average_lenght_of_adjectives(book): #средняя длина прилагательных
    nouns = get_lemma_part_speech(book, 'ADJ')
    count = 0
    for noun in nouns:
        count += len(noun)
    return count/len(nouns)

def average_lenght_of_adverbs(book): #средняя длина наречий
    nouns = get_lemma_part_speech(book, 'ADV')
    count = 0
    for noun in nouns:
        count += len(noun)
    return count/len(nouns)

def average_lenght_of_verbs(book): #средняя длина глаголов
    nouns = get_lemma_part_speech(book, 'VERB')
    count = 0
    for noun in nouns:
        count += len(noun)
        count += len(noun)
    return count/len(nouns)

def correlation_of_short_long_words(doc): #отношение коротких слов к длинным. на вход принимает произведения
    short = 0
    long = 0
    words = get_words(doc)
    for word in words:
        if len(word) < 5:
            short += 1
        elif len(word) > 8:
            long += 1
    return short / long

def correlation_of_long_medium_words(doc):
    long = 0
    medium = 0
    words = get_words(doc)
    for word in words:
        if  4 <= len(word) <= 8:
            medium += 1
        elif len(word) > 8:
            long += 1
    return long / medium
#%%
def semicolon_freq(doc):
    return doc.text.count(';') / len(doc.text)
#%%
def count_upper_words(doc):
    count = 0
    words = get_words(doc)
    for word in words:
        if word.isupper() == True:
            count += 1
    return count
#%%
def freq_of_freq_word(doc):
    temp = defaultdict(int)
    words = get_words(doc)
    for word in words:
        temp[word] += 1
    w = max(temp, key=temp.get)
    return words.count(w)
#%%
def freq_word_from_adjective(doc):
    adjectives = get_lemma_part_speech(doc, 'ADJ')
    temp = defaultdict(int)
    for word in adjectives:
        temp[word] += 1
    w = max(temp, key=temp.get)
    return adjectives.count(w) / len(adjectives)
#%%
def freq_word_from_noun(doc):
    nouns = get_lemma_part_speech(doc, 'NOUN')
    temp = defaultdict(int)
    for word in nouns:
        temp[word] += 1
    w = max(temp, key=temp.get)
    return nouns.count(w) / len(nouns)
#%%
def freq_word_from_verbs(doc):
    verbs = get_lemma_part_speech(doc, 'VERB')
    temp = defaultdict(int)
    for word in verbs:
        temp[word] += 1
    w = max(temp, key=temp.get)
    return verbs.count(w) / len(verbs)

def freq_of_space(doc) -> float:
    text = doc.text
    return text.count(' ') / len(text)

def sentences_avg_len_symbols(doc) -> float:
    sentences = get_sents(doc)
    return len(''.join(sentences).replace(' ', '')) / len(sentences)

def capitalized_words_count_without_start_of_sentences(doc) -> int:
    sentences = get_sents(doc)
    capital_letters = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    count = 0
    for sentence in sentences:
        for i in range(1, len(sentence)):
            letter_prev = sentence[i - 1]
            letter_curr = sentence[i]
            if letter_prev == ' ' and letter_curr in capital_letters:
                count += 1
    return count

def avg_syllable_per_noun(doc) -> float:
    nouns = get_lemma_part_speech(doc, 'NOUN')
    vowels = 'аеёиоуыэюя'
    syllable_count = 0
    for noun in nouns:
        for letter in noun:
            if letter in vowels:
                syllable_count += 1
    return syllable_count / len(nouns)

def avg_syllable_per_verb(doc) -> float:
    verbs = get_lemma_part_speech(doc, 'VERB')
    vowels = 'аеёиоуыэюя'
    syllable_count = 0
    for verb in verbs:
        for letter in verb:
            if letter in vowels:
                syllable_count += 1
    return syllable_count / len(verbs)

def avg_syllable_per_adjective(doc) -> float:
    adjectives = get_lemma_part_speech(doc, 'ADJ')
    vowels = 'аеёиоуыэюя'
    syllable_count = 0
    for adjective in adjectives:
        for letter in adjective:
            if letter in vowels:
                syllable_count += 1
    return syllable_count / len(adjectives)

def avg_syllable_per_adverb(doc) -> float:
    adverbs = get_lemma_part_speech(doc, 'ADV')
    vowels = 'аеёиоуыэюя'
    syllable_count = 0
    for adverb in adverbs:
        for letter in adverb:
            if letter in vowels:
                syllable_count += 1
    return syllable_count / len(adverbs)

def count_words_infinitive(doc):
    words = get_words(doc)
    # lem_new = ' '.join(get_lemma_words(doc))
    lem = get_words(get_doc(' '.join(get_lemma_words(doc))))
    count_infinitive = 0
    for x in range(len(words)):
        for y in range(len(lem)):
            if x == y:
                if words[x] == lem[y]:
                    count_infinitive += 1
    return count_infinitive

def freq_of_preps(book): #частота предлогов
    count = 0
    preps = ['без', 'безо', 'близ', 'в', 'во', 'вместо', 'вне', 'для', 'до', 'за', 'из', 'изо', 'из-за', 'из-под', 'к', 'ко', 'кроме', 'между', 'меж', 'на', 'над', 'надо', 'о', 'об', 'обо', 'от', 'ото', 'перед', 'передо', 'пред', 'предо', 'по', 'под', 'подо', 'при', 'про', 'ради', 'с', 'со', 'сквозь', 'среди', 'у', 'через', 'чрез']
    words = get_words(book)
    for word in words:
        if word in preps: count += 1
    return count/len(words)

def freq_of_unions(book): #частота союзов
    count = 0
    unions = ['а', 'вдобавок', 'именно', 'также', 'то', 'благодаря', 'благо', 'буде', 'будто', 'вдобавок', 'в результате', 'в связи', 'в силу', 'в случае', 'если', 'в то время', 'в том случае', 'ввиду', 'вопреки', 'вроде', 'вследствие', 'да','еще', 'и', 'ито', 'дабы', 'даже', 'даром', 'для того', 'же', 'едва', 'ежели', 'если бы', 'затем', 'зато', 'все же', 'и значит', 'а именно',' и поэтому', 'и притом', 'и все-таки', 'и следовательно', 'и то', 'и тогда', 'и еще', 'кабы', 'как будто', 'как если бы', 'словно', 'как только', 'коли', 'к тому же', 'кроме того', 'либо', 'между тем', 'не столько','но даже', 'невзирая на', 'независимо от', 'несмотря на', 'перед тем', 'по мере того', 'по причине', 'подобно тому', 'пока', 'покамест', 'покуда', 'пока', 'не после того', 'поскольку', 'потому', 'потому что', 'почему', 'прежде', 'при всем том', 'при условии', 'притом', 'причем', 'пускай', 'пусть', 'ради', 'раз', 'раньше чем', 'с тех пор', 'так что', 'тогда как', 'то есть', 'то ли', 'тоже', 'только', 'только бы', 'только что', 'только лишь', 'только чуть', 'точно', 'хотя', 'чтоб', 'чтобы']
    words = get_words(book)
    for word in words:
        if word in unions: count += 1
    return count/len(words)
