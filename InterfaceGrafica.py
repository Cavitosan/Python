from tkinter import *
import os

c = os.path.dirname(__file__)
nomeArquivo = c+"\\nomes.txt"


def gravarDados():
    arquivo = open(nomeArquivo, "a")
    arquivo.write("\nNome......: %s" % vnome.get())
    arquivo.write("\nTelefone..: %s" % vfone.get())
    arquivo.write("\nEmail.....: %s" % vemail.get())
    arquivo.write("\nOBS.......: %s" % vobs.get("1.0", END))
    arquivo.write("\n\n")
    arquivo.close()
    pass


app = Tk()
app.title("CFB Cursos")  # titulo
app.geometry("500x300")  # tamanho da tela
app.configure(background="#dde")

txt1 = Label(app, text="Curso de Python", background="#ff0", foreground="#000")
# txt1.place(x=10, y=10, width=100, height=20)

# anchor => N=Norte S=South W=West E=East
# Também podemos usar NE = Nordeste, SE = Sudeste, NO = Noroeste, SO = Sudoeste
# Nome:
lb1 = Label(app, text="Nome", background="#dde", foreground="#009", anchor=W)
lb1.place(x=10, y=10, width=100, height=20)
vnome = Entry(app)
vnome.place(x=10, y=30, width=200, height=20)

# Telefone:
lb2 = Label(app, text="Telefone", background="#dde",
            foreground="#009", anchor=W)
lb2.place(x=10, y=60, width=100, height=20)
vfone = Entry(app)
vfone.place(x=10, y=80, width=200, height=20)

# Email:
lb3 = Label(app, text="Email", background="#dde",
            foreground="#009", anchor=W)
lb3.place(x=10, y=110, width=100, height=20)
vemail = Entry(app)
vemail.place(x=10, y=130, width=200, height=20)

lb4 = Label(app, text="Observações", background="#dde",
            foreground="#009", anchor=W)
lb4.place(x=10, y=160, width=100, height=20)
vobs = Text(app)
vobs.place(x=10, y=180, width=300, height=80)


vtxt = "Módulo Tkinter"
vbg = "#ff0"  # azul
vfg = "#000"

# txt2 = Label(app, text=vtxt, bg=vbg, fg=vfg)
# txt2.pack(ipadx=20, ipady=20, padx=5, pady=5, side="top",
#          fill=X, expand=True)  # pack = container

btn = Button(app, text="Gravar", command=gravarDados)
btn.place(x=10, y=260, width=100, height=30)

app.mainloop()  # já gera uma janela
