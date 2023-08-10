import random


def cadastrar_palavra(lista, palavra):
    lista.append(palavra)
    print(f"Palavra '{palavra}' cadastrada com sucesso!")


def consultar_palavra(lista, palavra):
    if palavra in lista:
        print(f"A palavra '{palavra}' está na lista.")
    else:
        print(f"A palavra '{palavra}' não está na lista")


def excluir_palavra(lista, palavra):
    if palavra in lista:
        lista.remove(palavra)
        print(f"Palavra '{palavra}' excluída com sucesso!")
    else:
        print(f"Palavra '{palavra}' não está na lista.")


lista_palavras = []

while (True):
    print("\nMenu: ")
    print("1. Cadastrar palavra")
    print("2. Consultar palavra")
    print("3. Excluir palavra")
    print("4. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nova_palavra = input("Digite a palavra para cadastrar: ")
        cadastrar_palavra(lista_palavras, nova_palavra)
    elif escolha == "2":
        palavra_consulta = input("Digite a palavra para consultar: ")
        consultar_palavra(lista_palavras, palavra_consulta)
    elif escolha == "3":
        palavra_excluir = input("Digite a palvra a ser excluída: ")
        excluir_palavra(lista_palavras, palavra_excluir)
    elif escolha == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
