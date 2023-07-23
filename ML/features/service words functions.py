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





def podo(text):
    text = text.lower()
    return text.count('подо') / len(text)
def pri(text):
    text = text.lower()
    return text.count('при') / len(text)
def pro(text):
    text = text.lower()
    return text.count('про') / len(text)
def co(text):
    text = text.lower()
    return text.count('со') / len(text)
def skvoz(text):
    text = text.lower()
    return text.count('сквозь') / len(text)
def sredi(text):
    text = text.lower()
    return text.count('среди') / len(text)
def ot(text):
    text = text.lower()
    return text.count('от') / len(text)
def oto(text):
    text = text.lower()
    return text.count('ото') / len(text)
def krome(text):
    text = text.lower()
    return text.count('кроме') / len(text)
def vne(text):
    text = text.lower()
    return text.count('вне') / len(text)
def peredo(text):
    text = text.lower()
    return text.count('передо') / len(text)
def vdobavok(text):
    text = text.lower()
    return text.count('вдобавок') / len(text)
def imenno(text):
    text = text.lower()
    return text.count('именно') / len(text)
def takje(text):
    text = text.lower()
    return text.count('также') / len(text)
def to(text):
    text = text.lower()
    return text.count('то') / len(text)
def blagodary(text):
    text = text.lower()
    return text.count('благодаря') / len(text)
def blago(text):
    text = text.lower()
    return text.count('благо') / len(text)
def budto(text):
    text = text.lower()
    return text.count('будто') / len(text)
def v_rezyltate(text):
    text = text.lower()
    return text.count('в результате') / len(text)
def v_svyzi(text):
    text = text.lower()
    return text.count('в связи') / len(text)
def v_sily(text):
    text = text.lower()
    return text.count('в силу') / len(text)
def v_slychae(text):
    text = text.lower()
    return text.count('в случае') / len(text)
def esli(text):
    text = text.lower()
    return text.count('если') / len(text)
def v_to_vremy(text):
    text = text.lower()
    return text.count('в то время') / len(text)
def v_tom_slychae(text):
    text = text.lower()
    return text.count('в том случае') / len(text)
def vvidu(text):
    text = text.lower()
    return text.count('ввиду') / len(text)
def vsledstvie(text):
    text = text.lower()
    return text.count('вследствие') / len(text)
def eshe(text):
    text = text.lower()
    return text.count('ещё') / len(text)


list_functions = [freq_ellipsis, bliz, bezo, chrez, izo, s_tex_por, tolko_losh, nesmotry_na, obo, cherez,
                  puskay, podobno_tomu, nevziraia_na, libo, i_vse_taki, i_sledovatelno, vopreki, vrode,
                  slovno, kak_esly_bi, po_prichine, poskolky, radi, podo, pri, pro, co, skvoz, sredi, ot, oto, krome,
                  vne, peredo, vdobavok, imenno, takje, to, blagodary, blago, budto, v_rezyltate, v_svyzi, v_sily, v_slychae,
                  esli, v_to_vremy, v_tom_slychae, vvidu, vsledstvie, eshe]
