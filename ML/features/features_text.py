def freq_ellipsis(text):
    return text.count('...') / len(text)
#%%
def bezo(text):
    text = text.lower()
    return text.count('безо') / len(text)
#%%
def bliz(text):
    text = text.lower()
    return text.count('близ') / len(text)
#%%
def chrez(text):
    text = text.lower()
    return text.count('чрез') / len(text)
#%%
def izo(text):
    text = text.lower()
    return text.count('изо') / len(text)
#%%
def s_tex_por(text):
    text = text.lower()
    return text.count('с тех пор') / len(text)
#%%
def tolko_losh(text):
    text = text.lower()
    return text.count('только лишь') / len(text)
#%%
def nesmotry_na(text):
    text = text.lower()
    return text.count('несмотря на') / len(text)

def avg_words_between_commas(text):
    words_count_sum = 0
    words_between = text.split(',')
    for words in words_between:
        words_count_sum += len(words.split(' '))
    return words_count_sum / len(words_between)

func_text = [avg_words_between_commas, freq_ellipsis, bliz, bezo, chrez, izo, s_tex_por, tolko_losh, nesmotry_na]

def get_feature_text(doc):
    text = doc.text
    text_features = [func(text) for func in func_text]
    return text_features
