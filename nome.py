from automato import *

maiuscula = "[A-Z|Á|À|Â|Ã|É|È|Ê|Í|Ó|Ô|Õ|Ú|Ç|Ñ|-]"
minuscula = "[a-z|á|à|â|ã|é|è|ê|í|ó|ô|õ|ú|ç|ñ|-]"

nome = {0: {maiuscula: 1},
        1: {maiuscula: 1, minuscula: 1, '\.': 2, ' ': 0},
        2: {' ': 0}}
finais = [1,2]

print(aceita(nome, 0, finais, 'André'))