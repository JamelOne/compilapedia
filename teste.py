from automato import *
import re

texto = "Caio Júlio César (em latim: Caius ou Gaius Iulius Caesar) foi um patrício, líder militar e político romano."

maiuscula = "[A-Z|Á|À|Â|Ã|É|È|Ê|Í|Ó|Ô|Õ|Ú|Ç|Ñ|-]"
minuscula = "[a-z|á|à|â|ã|é|è|ê|í|ó|ô|õ|ú|ç|ñ|-]"

nome = {0: {maiuscula: 1},
        1: {maiuscula: 1, minuscula: 1, '\.': 2, ' ': 0},
        2: {' ': 0}}

artigo = {0: {"[O|o|A|a]": 1, "[U|u]":2},
            1: {"[s]": 5},
            2: {"[n]": 3, "[m]": 4},
            3: {"[s]": 5},
            4: {"[a]": 1},
            5: {}}

separadores = {0: {"e": 1, ",": 1},
         1: {}}

final = {0: {"\.": 1},
         1: {}}

adjetivo = {0: {minuscula: 1},
        1: {minuscula: 2},
        2: {minuscula: 2}}

list_regra = [nome,artigo,separadores,final,adjetivo]
list_finais = [[1,2],[1,4,5],[1],[1],[2]]
texto_retorno = ["NOME", "ARTIGO", "SEPARADOR", "FINAL", "ADJETIVO"]

texto = re.sub("[\(\[].*?[\)\]]", "", texto)
lista = texto.split()

strings = list()

for palavra in lista:
        if(re.match(".*\,", palavra)):
                strings.extend(palavra.rpartition(",")[0:2])
        elif(re.match(".*\.", palavra)):
                strings.extend(palavra.rpartition(".")[0:2])
        else:
                strings.append(palavra)
print(strings)

list_tokens = list()

for elem in strings:
        if(re.match("^(é|era|foi)$",elem)):
                list_tokens.append("VERBO")
        else:        
                for i in range(len(list_regra)):
                        if(aceita(list_regra[i], 0, list_finais[i], elem)):
                                list_tokens.append(texto_retorno[i])
                                break

print(list_tokens)

