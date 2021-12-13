import tkinter as tk
from tkinter import scrolledtext
import nome, artigo, separadores, final, adjetivo, automato
import time, re
list_regra = [nome.automato,artigo.automato,separadores.automato,
                final.automato,adjetivo.automato]
list_finais = [nome.finais,artigo.finais,separadores.finais,
                final.finais,adjetivo.finais]
texto_retorno = ["NOME", "ARTIGO", "SEPARADOR", "FINAL", "ADJETIVO"]

def analisarLexico(lista_palavras):
     # Removendo o \n do final.
    if lista_palavras[-1][:-1]=='\n':
        lista_palavras[-1] = lista_palavras[-1][:-1]
    
    
    # Separando pontos e vírgulas de caracteres
    lista_final = []
    for palavra in lista_palavras:
        if(re.match(".*\,", palavra)):
                lista_final.extend(palavra.rpartition(",")[:2])                
        elif(re.match(".*\.", palavra)):
                lista_final.extend(palavra.rpartition(".")[:2])
        else:
                lista_final.append(palavra)

    # Reconhecendo à qual regra pertence cada palavra
    list_tokens = list()
    texto = ''
    for elem in lista_final:
        if(re.match("^(é|era|foi)$",elem)):
            list_tokens.append({
                    'tipo':'VERBO',
                    'conteudo':elem})
            texto+=f'"{elem}" : VERBO\n'
        else:
            for i in range(len(list_regra)):
                if(automato.aceita(list_regra[i], 0, list_finais[i], elem)):
                    list_tokens.append({
                        'tipo':texto_retorno[i],
                        'conteudo':elem})
                    texto+=f'"{elem}" : {texto_retorno[i]}\n'
                    break
    
    # FRONTEND
    labelLex.configure(text='Anls. Léxico\n'+texto)
    with open('Output.txt', 'a') as f:
        f.write('\nInício do Analisador Léxico:\n')
        f.write(texto)
        f.close()
    return list_tokens

def analisadorSintatico(lista_tokens):
    # Fazendo a junção de elementos de tipo igual
    # que estão adjacentes, como NOME,NOME e ADJETIVO,ADJETIVO
    lista_processada = []
    ultimo_token = None
    temp_token = None
    for token in lista_tokens:
        if ultimo_token and token['tipo']==ultimo_token['tipo']:
            temp_token['conteudo'] += ' '+token['conteudo']
        else:
            if temp_token: lista_processada.append(temp_token)
            temp_token = token
            if(temp_token == lista_tokens[-1]): lista_processada.append(temp_token)
        ultimo_token = token
    
    texto = ''
    for elem in lista_processada:
            texto+=str(elem)+'\n'
    

    # Checando se a cadeia pode ser considerada válida
    # segundo o padrão aceito pela linguagem
    cadeia_valida_automato = {
        0: {"NOME": 1},
        1: {"VERBO": 2},
        2: {'ARTIGO': 3, "ADJETIVO": 3},
        3: {'FINAL': 4, 'SEPARADOR': 2, 'ADJETIVO': 3},
        4:{},
        }
    cadeia_valida_finais = [4]
    res = bool()
    if(automato.aceita(cadeia_valida_automato, 0, 
        cadeia_valida_finais, [x['tipo'] for x in lista_processada])):
        res = True
        texto+='A cadeia é uma cadeia válida!\n'
    else:
        res = False
        texto+='A cadeia não é uma cadeia válida!\n'
    
    # FRONTEND
    labelSint.configure(text='Anls. Sintático\n'+texto)
    with open('Output.txt', 'a') as f:
        f.write('\nInício do Analisador Sintático:\n')
        f.write(texto)
        f.close()
    return res

def clickMe():
    # FRONTEND
    texto = nameEntered.get('1.0', 'end')
    with open('Output.txt', 'a') as f:
        f.write('\nInício do Processamento - Texto Original: ')
        f.write(texto)
        f.close() 
    
    # Removendo informações entre parênteses e afins
    texto = re.sub("[\(\[].*?[\)\]]", "", texto)
    
    # Separando palavra por palavra numa lista
    lista_palavras = texto.split()
    lista_tokens=analisarLexico(lista_palavras)
    acceptable = analisadorSintatico(lista_tokens)
    with open('Output.txt', 'a') as f:
        f.write('\n\n\n')
        f.close()



window = tk.Tk()
window.title("Python Tkinter Text Box")

labelLex = tk.Label(window, text = "Anls. Léxico\n")
labelLex.grid(row=2, column=0)

labelSint = tk.Label(window, text = "Anls. Sintático\n")
labelSint.grid(row=2, column=1)
 
nameEntered = scrolledtext.ScrolledText(window, width=70, height=10)
nameEntered.grid(row=1, column=0, columnspan=2)

button = tk.Button(window, text = "Click Me", command = clickMe)
button.grid(row=0, column=0, columnspan=2)


window.mainloop()