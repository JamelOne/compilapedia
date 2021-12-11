from automato import *

verbo = {0: {" ": 1, ",": 2},
         1: {"e": 2},
         2: {" ": 3},
         3: {}}
finais = [3]

x = print(aceita(verbo, 0, finais, ' e '))