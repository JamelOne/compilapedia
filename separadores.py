from automato import *

separadores = {0: {" ": 1, ",": 2},
         1: {"e": 2},
         2: {" ": 3},
         3: {}}
finais = [3]

x = print(aceita(separadores, 0, finais, ' e '))