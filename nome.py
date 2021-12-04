import re

txt = "Caio Júlio César[a] (em latim: Caius ou Gaius Iulius Caesar ou\
    IMP•C•IVLIVS•CÆSAR•DIVVS;[1] 13 de julho de 100 a.C.[b] – 15 de \
    março de 44 a.C.[c]) foi um patrício, líder militar e político romano."

#_regex = {'minuscula': "[a-z|á|à|â|ã|é|è|ê|í|ó|ô|õ|ú|ç|ñ|-]",
#        'maiuscula': "[A-Z|A|À|Â|Ã|É|È|Ê|Í|Ó|Ô|Õ|Ú|Ç|Ñ|-]",
#        '.': ".",
#        ' ': " "}

maiuscula = "[A-Z|A|À|Â|Ã|É|È|Ê|Í|Ó|Ô|Õ|Ú|Ç|Ñ|-]"
minuscula = "[a-z|á|à|â|ã|é|è|ê|í|ó|ô|õ|ú|ç|ñ|-]"

nome = {0: {maiuscula: 1},
        1: {maiuscula: 1, minuscula: 1, '.': 2},
        2: {' ': 0}}

finais = [1,2]

def transicao(estado, entrada):
    for transicao in estado.keys():
        if re.match(transicao, entrada): return estado[transicao]
    return False

def aceitaNome(automato, inicial, finais, string):
    estado = inicial
    for char in string:
        ok = transicao(automato[estado], char)
        if ok == False: return False
        else: estado = ok
    return estado in finais

x = aceitaNome(nome, 0, finais, 'Nome~')
print(x)