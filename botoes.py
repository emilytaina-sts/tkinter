import tkinter as tk

def clicado(i):
    global contador
    contador+= i
    texto.config(text=f"Você pressionou o botão{contador} vezes!")

contador = 0

janela = tk.Tk()
janela.geometry("200x200")
 
texto = tk.Label(text=f"Você não apertou o botâo ainda :(")
texto.pack()

botao = tk.Button(text="Clique aqui!",command=lambda:clicado(2))
botao.pack()


janela.mainloop()