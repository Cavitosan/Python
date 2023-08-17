import matplotlib.pyplot as plt

nomes = []
datas_nascimento = []
sexos = []

num_pessoas = int(input("Quantas pessoas deseja incluir no relatório? "))

for _ in range(num_pessoas):
    nome = input("Nome da pessoa: ")
    data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
    sexo = input("Sexo (M/F): ")

    nomes.append(nome)
    datas_nascimento.append(datas_nascimento)
    sexos.append(sexo)

quantidades = {'M': 0, 'F': 0}
for sexo in sexos:
    quantidades[sexo] += 1

plt.bar(quantidades.keys(), quantidades.values())
plt.xlabel('Sexo')
plt.ylabel('Quantidade')
plt.title('Relatório de Sexo')
plt.show()
