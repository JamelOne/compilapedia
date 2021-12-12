import tkinter as tk
from tkinter import scrolledtext
import nome, artigo, separadores, final, adjetivo, automato
import time, re
list_regra = [nome.automato,artigo.automato,separadores.automato,
                final.automato,adjetivo.automato]
list_finais = [nome.finais,artigo.finais,separadores.finais,
                final.finais,adjetivo.finais]
texto_retorno = ["NOME", "ARTIGO", "SEPARADOR", "FINAL", "ADJETIVO"]

def julioCesar():
    julioCesar = "Caio Júlio César (em latim: Caius ou Gaius Iulius Caesar) foi um patrício, líder militar e político romano." 
    nameEntered.setvar(julioCesar)
def analisarLexico(lista_palavras):
    print(lista_palavras)
    if lista_palavras[-1][:-1]=='\n':
        lista_palavras[-1] = lista_palavras[-1][:-1] # Removendo o \n do final.
    
    lista_final = []
    for palavra in lista_palavras:
        if(re.match(".*\,", palavra)):
                lista_final.extend(palavra.rpartition(",")[:2])                
        elif(re.match(".*\.", palavra)):
                lista_final.extend(palavra.rpartition(".")[:2])
        else:
                lista_final.append(palavra)
    print(lista_final)

    list_tokens = list()
    texto = ''
    for elem in lista_final:
        if(re.match("^(é|era|foi)$",elem)):
            list_tokens.append({
                    'tipo':'VERBO',
                    'conteudo':elem})
        else:
            for i in range(len(list_regra)):
                if(automato.aceita(list_regra[i], 0, list_finais[i], elem)):
                    list_tokens.append({
                        'tipo':texto_retorno[i],
                        'conteudo':elem})
                    texto+=f'"{elem}":{texto_retorno[i]}\n'
                    break
    label.configure(text=texto)
    print(list_tokens)
def clickMe():
     # ############################################
     #                   INÍCIO                  #
     #               ANALISADOR LÉXICO          #
    # ############################################
    
    texto = nameEntered.get('1.0', 'end')
    texto = re.sub("[\(\[].*?[\)\]]", "", texto)
    lista_palavras = texto.split()
    analisarLexico(lista_palavras)
    # ############################################
     #                   INÍCIO                  #
     #               ANALISADOR SINTÁTICO        #
    # ############################################
    

 

window = tk.Tk()
window.title("Python Tkinter Text Box")

label = tk.Label(window, text = "Insira o texto!\n")
label.pack(side=tk.BOTTOM)
 
nameEntered = scrolledtext.ScrolledText(window, width=70, height=10)
nameEntered.pack(side=tk.BOTTOM)

button = tk.Button(window, text = "Click Me", command = clickMe)
button.pack(side=tk.BOTTOM)


window.mainloop()