import re

def maiuscula(char):
    find = re.findall("[A-ZÁÁÁÂÃÉÊÍÓÔÕÚÇÑ-]", char)
    if find:
        print("Found")
    else:
        print("Not found")

def minuscula(char):
    find = re.findall("[a-záàâãéèêíóôõúçñ-]", char)
    if find:
        return True
    else:
        return False

dfa = {0:{'0':1},
       1:{'0':1, '1':1, '2':2, '3':0},
       2:{'4':0}}

def nome(str):
    tam = len(str)
    if maiuscula(str[0]):
        for i in range(tam):


def accepts(transitions,initial,accepting,str):
    state = initial
    if(maiuscula(str[0]):
        for c in str:
            if(minuscula(c) or maiuscula(c)):
                op = 0
            if(maiuscula(c)):
                op = 0
            state = transitions[state][op]
        return state in accepting
    else:
        return False

>>> accepts(dfa,0,{0},'1011101')
True
>>> accepts(dfa,0,{0},'10111011')
False