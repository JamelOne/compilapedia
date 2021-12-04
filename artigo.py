import re

txt = "Caio Júlio César[a] (em latim: Caius ou Gaius Iulius Caesar ou\
    IMP•C•IVLIVS•CÆSAR•DIVVS;[1] 13 de julho de 100 a.C.[b] – 15 de \
    março de 44 a.C.[c]) foi um patrício, líder militar e político romano."

def transicao(estado, entrada):
    for transicao in estado.keys():
        if re.match(transicao, entrada): 
            return estado[transicao]
    return False

def aceitaArtigo(string):
    artigo = {0: {"[O|o|A|a]": 1, "[U|u]":2},
            1: {"[s]": 5},
            2: {"[n]": 3, "[m]": 4},
            3: {"[s]": 5},
            4: {"[a]": 1}}

    finais = [1,4,5]
    estado = 0
    for char in string:
        if(estado == 5):
            return False 
        ok = transicao(artigo[estado], char)
        if ok == False: return False
        else: estado = ok
    return estado in finais

x = aceitaArtigo('umas')
print(x)