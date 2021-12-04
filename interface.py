import tkinter as tk
from tkinter import scrolledtext
window = tk.Tk()
 
window.title("Python Tkinter Text Box")

 
def clickMe():
    label.configure(text= 'Texto: ' + nameEntered.get('1.0', 'end'))
 
label = tk.Label(window, text = "Insira o texto!\n")
# label.grid(column = 0, row = 0)
label.pack(side=tk.BOTTOM)
 
name = tk.StringVar()
# nameEntered = tk.Entry(window, width = 70, textvariable = name)
nameEntered = scrolledtext.ScrolledText(window, width=70, height=10)
# nameEntered.grid(column = 0, row = 1)
nameEntered.pack(side=tk.BOTTOM)

 
 
button = tk.Button(window, text = "Click Me", command = clickMe)
# button.grid(column= 0, row = 2)
button.pack(side=tk.BOTTOM)
 
window.mainloop()