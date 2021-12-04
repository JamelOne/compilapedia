import tkinter as tk
from tkinter import scrolledtext
window = tk.Tk()
 
window.title("Python Tkinter Text Box")

 
def clickMe():
    texto = nameEntered.get('1.0', 'end')
    label.configure(text= 'Texto: ' + texto)
    palabras = texto.split(sep=" ")
    palabras[-1] = palabras[-1][:-1]
    print(palabras)
    # for palabra in palabras:
    #     if(aceitaNome(palabra)):
    #         return {
    #             'tipo': 'nome',
    #             'conteudo':palabra
    #         }
    #     if(aceitaVerbo(palabra)):
    #         return {
    #             'tipo': 'verbo',
    #             'conteudo':palabra
    #         }
    #     return False
    

 
label = tk.Label(window, text = "Insira o texto!\n")
label.pack(side=tk.BOTTOM)
 
nameEntered = scrolledtext.ScrolledText(window, width=70, height=10)
nameEntered.pack(side=tk.BOTTOM)

button = tk.Button(window, text = "Click Me", command = clickMe)
button.pack(side=tk.BOTTOM)
 
window.mainloop()