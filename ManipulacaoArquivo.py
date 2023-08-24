# Em Python, o uso do ';' pode atrapalhar a execução do código
# Não utilize, em Python, o ';'

def escrever_arquivo(nome_arquivo, conteudo):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(conteudo)


def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        return conteudo


def adicionar_em_arquivo(nome_arquivo, novo_conteudo):
    with open(nome_arquivo, 'a') as arquivo:
        arquivo.write(novo_conteudo)


def main():
    nome_arquivo = 'exemplo.txt'

    # Escrever no arquivo
    conteudo = "Olá, este é um exemplo de manipulação de arquivos em Python."
    escrever_arquivo(nome_arquivo, conteudo)

    # Ler e exibir o conteúdo do arquivo
    conteudo_lido = ler_arquivo(nome_arquivo)
    print("Conteúdo do arquivo:")
    print(conteudo_lido)

    # Adicionar mais conteúdo ao arquivo
    novo_conteudo = "\nEste é um novo conteúdo adicionado ao arquivo.\n"
    adicionar_em_arquivo(nome_arquivo, novo_conteudo)

    # Ler e exibir o conteúdo atualizado do arquivo
    conteudo_atualizado = ler_arquivo(nome_arquivo)
    print("\nConteúdo atualizado do arquivo:\n")
    print(conteudo_atualizado)


if __name__ == "__main__":
    main()
