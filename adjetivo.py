from automato import *

minuscula = "[a-z|á|à|â|ã|é|è|ê|í|ó|ô|õ|ú|ç|ñ|-]"

adjetivo = {0: {minuscula: 1},
        1: {minuscula: 2},
        2: {minuscula: 2}}
finais = [2]

x = print(aceita(adjetivo, 0, finais, 'bonito'))