import tkinter as tk
from tkinter import scrolledtext
import nome,artigo,separadores,final,adjetivo,re,automato
list_regra = [nome.automato,artigo.automato,separadores.automato,
                final.automato,adjetivo.automato]
list_finais = [nome.finais,artigo.finais,separadores.finais,
                final.finais,adjetivo.finais]
texto_retorno = ["NOME", "ARTIGO", "SEPARADOR", "FINAL", "ADJETIVO"]
def clickMe():

     # ############################################
     #                   INÍCIO                  #
     #               ANALISADOR LÉXICO          #
    # ############################################
    
    texto = nameEntered.get('1.0', 'end')
    # label.configure(text= 'Texto: ' + texto)
    texto = re.sub("[\(\[].*?[\)\]]", "", texto)
    lista_auxiliar = texto.split()
    print(lista_auxiliar)
    if lista_auxiliar[-1][:-1]=='\n':
        lista_auxiliar[-1] = lista_auxiliar[-1][:-1] # Removendo o \n do final.
    print(lista_auxiliar)
    lista_final = []
    for palavra in lista_auxiliar:
        if(re.match(".*\,", palavra)):
                lista_final.extend(palavra.rpartition(",")[:2])                
        elif(re.match(".*\.", palavra)):
                lista_final.extend(palavra.rpartition(".")[:2])
        else:
                lista_final.append(palavra)
    print(lista_final)
    list_tokens = list()
    for elem in lista_final:
            if(re.match("^(é|era|foi)$",elem)):
                list_tokens.append("VERBO")
            else:        
                for i in range(len(list_regra)):
                    if(automato.aceita(list_regra[i], 0, list_finais[i], elem)):
                        list_tokens.append(texto_retorno[i])
                        print(f'A cadeia "{elem}" foi aceita como um {texto_retorno[i]}')
                        break

    print(list_tokens)

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