import re

def transicao(estado, entrada):
    for transicao in estado.keys():
        if re.match(transicao, entrada):
            return estado[transicao]
    return False

def aceita(automato, inicial, finais, cadeia):
    estado = inicial
    print('cadeia: '+str(cadeia))
    for caractere in cadeia:
        print('caractere:'+str(caractere))
        if(not automato[estado]): return False
        ok = transicao(automato[estado], caractere)
        if ok == False: return False
        else: estado = ok
    return estado in finais