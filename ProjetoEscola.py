import tkinter as tk
from tkinter import messagebox


class Escola:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_alunos(self):
        return self.alunos


class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"


nome_entry = None
idade_entry = None
aluno_listbox = None


def adicionar_aluno():
    nome = nome_entry.get()
    idade = idade_entry.get()

    if nome and idade:
        aluno = Aluno(nome, idade)
        escola.adicionar_aluno(aluno)
        aluno_listbox.insert(tk.END, aluno)
        nome_entry.delete(0, tk.END)
        idade_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Preencha todos os campos!")


def main():

    global escola, nome_entry, idade_entry, aluno_listbox

    escola = Escola()

    root = tk.Tk()
    root.title("Simulação de Escola")

    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    nome_label = tk.Label(frame, text="Nome do Aluno: ")
    nome_label.grid(row=0, column=0)

    idade_label = tk.Label(frame, text="Idade do Aluno: ")
    idade_label.grid(row=1, column=0)

    nome_entry = tk.Entry(frame)
    nome_entry.grid(row=0, column=1)

    idade_entry = tk.Entry(frame)
    idade_entry.grid(row=1, column=1)

    adicionar_button = tk.Button(
        frame, text="Adicionar Aluno", command=adicionar_aluno)
    adicionar_button.grid(row=2, column=0, columnspan=2)

    aluno_listbox = tk.Listbox(frame)
    aluno_listbox.grid(row=3, column=0, columnspan=2)

    root.mainloop()


if __name__ == "__main__":
    main()
