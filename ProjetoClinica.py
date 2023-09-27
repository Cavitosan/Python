class Paciente:
    def __init__(self, nome, idade, sintomas):
        self.nome = nome
        self.idade = idade
        self.sintomas = sintomas

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, sintomas: {self.sintomas}"


class Clinica:
    def __init__(self):
        self.pacientes = []

    def adicionar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def listar_pacientes(self):
        for paciente in self.pacientes:
            print(paciente)


def menu():
    print("Bem-vindo à Clínica Médica")
    print("1. Adicionar paciente")
    print("2. Listar pacientes")
    print("3. Sair")


def main():
    clinica = Clinica()

    while True:
        menu()
        opcao = input("Selecione uma opcao: ")

        if opcao == "1":
            nome = input("Nome do paciente: ")
            idade = input("Idade do paciente: ")
            sintomas = input("Sintomas do paciente: ")
            paciente = Paciente(nome, idade, sintomas)
            clinica.adicionar_paciente(paciente)
            print("Paciente adicionado com sucesso.")

        elif opcao == "2":
            print("Lista de Pacientes: ")
            clinica.listar_pacientes()

        elif opcao == "3":
            print("Obrigado por usar o sistema de nossa clínica.")
            break


if __name__ == "__main__":
    main()
