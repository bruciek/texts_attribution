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

def obo(text):
    text = text.lower()
    return text.count('обо') / len(text)
#%%
def cherez(text):
    text = text.lower()
    return text.count('через') / len(text)
#%%
def puskay(text):
    text = text.lower()
    return text.count('пускай') / len(text)
#%%
def podobno_tomu(text):
    text = text.lower()
    return text.count('подобно тому') / len(text)
#%%
def nevziraia_na(text):
    text = text.lower()
    return text.count('невзирая на') / len(text)
#%%
def libo(text):
    text = text.lower()
    return text.count('либо') / len(text)
#%%
def i_vse_taki(text):
    text = text.lower()
    return text.count('и все-таки') / len(text)
#%%
def i_sledovatelno(text):
    text = text.lower()
    return text.count('и следовательно') / len(text)
#%%
def vopreki(text):
    text = text.lower()
    return text.count('вопреки') / len(text)
#%%
def vrode(text):
    text = text.lower()
    return text.count('вроде') / len(text)
#%%
def slovno(text):
    text = text.lower()
    return text.count('словно') / len(text)
#%%
def kak_esly_bi(text):
    text = text.lower()
    return text.count('как если бы') / len(text)
#%%
def po_prichine(text):
    text = text.lower()
    return text.count('по причине') / len(text)
#%%
def poskolky(text):
    text = text.lower()
    return text.count('поскольку') / len(text)
#%%
def radi(text):
    text = text.lower()
    return text.count('ради') / len(text)

def avg_words_between_commas(text):
    words_count_sum = 0
    words_between = text.split(',')
    for words in words_between:
        words_count_sum += len(words.split(' '))
    return words_count_sum / len(words_between)

func_text = [freq_ellipsis, bliz, bezo, chrez, izo, s_tex_por, tolko_losh, nesmotry_na, obo, cherez,
                  puskay, podobno_tomu, nevziraia_na, libo, i_vse_taki, i_sledovatelno, vopreki, vrode,
                  slovno, kak_esly_bi, po_prichine, poskolky, radi, avg_words_between_commas]

def get_feature_text(doc):
    text = doc.text
    text_features = [func(text) for func in func_text]
    return text_features
