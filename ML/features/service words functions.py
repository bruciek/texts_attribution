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

list_functions = [freq_ellipsis, bliz, bezo, chrez, izo, s_tex_por, tolko_losh, nesmotry_na]