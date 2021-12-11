from automato import *

artigo = {0: {"[O|o|A|a]": 1, "[U|u]":2},
            1: {"[s]": 5},
            2: {"[n]": 3, "[m]": 4},
            3: {"[s]": 5},
            4: {"[a]": 1},
            5: {}}
finais = [1,4,5]

print(aceita(artigo, 0, finais, 'umas'))