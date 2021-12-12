from automato import *

verbo = {0: {"^(é|era|foi)$": 1},
         1: {}}
finais = [1]

x = print(aceita(verbo, 0, finais, 'era'))