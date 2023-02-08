'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
print ('Python - Aula23: Classes')

class Carro:
    velMax=0 #valores padrao caso o objeto não determine valores especificos
    ligado=False
    cor=""

c1=Carro()
c2=Carro()
c3=Carro()

c1.velMax=200
c1.cor="preto"
c1.ligado=False

print("Velocidade Maxima do Carro1: ", c1.velMax)
print("Cor do Carro1: ", c1.cor)
estado="sim" if c1.ligado else "nao"
print("Ligado do Carro1: ", c1.ligado)
print("Ligado do carro1 na variavel estado:", estado)

print("Python - Aula 24: Construtor e métodos")

#Construtor é um metodo que será chamado quando instanciarmos um objeto da Classe

class CarroF:
    velMax=0 #valores padrao caso o objeto não determine valores especificos
    ligado=False
    cor=""

    def __init__(self, vm, li, c):
        self.velMax = vm
        self.ligado = li
        self.cor = c
    
    def mostrar(self):
        print("Velocidade Maxima do Carro1: ", self.velMax)
        print("Cor do Carro...............: ", self.cor)
        estado="sim" if self.ligado else "N"
        print("Ligado do Carro............: ", estado)
        print("-------------------------------------")
    
    def ligar(self):
        self.ligado = True    
    def desligar(self):
        self.ligado = False
        
    def andar(self):
        if(self.ligado):
            print("Andando")
        else:
            print("Carro desligado")
    
    
c1 = CarroF(200, False, "Preto")
c2 = CarroF(120, False, "Branco")
c3 = CarroF(350, False, "Vermelho")

c1.ligar();
c1.mostrar();
c2.mostrar();
c3.mostrar();

c1.andar()
c2.andar()

print("Python Aula25: Herança")

#Classe que herda outra classe - classe pai e classe filho
#Todas as caracteristicas da classe pai são herdadas pela classe filho

class NPC: #Classe pai, base ou super
    def __init__(self, nome, time, forca, municao):
        self.nome = nome
        self.time = time
        self.forca = forca
        self.municao = municao
        self.vivo = True
        self.energia = 100
        
    def info(self):
        print("Nome.....:" + self.nome)
        print("Time.....:" + str(self.time))
        print("Forca....:" + str(self.forca))
        print("Municao..:" + str(self.municao))
        print("Vivo.....:" + ("Vivo: sim" if self.vivo else "Vivo: nao"))
        print("Energia..:" + str(self.energia))
        print("-------------------------------")
    
class Soldado(NPC): #classe filho
    def __init__(self, nome, time): #construtor para a classe filho sobreescreve o construtor da classe pai
        self.forca = 200
        self.municao = 200
        super().__init__(nome, time, self.forca, self.municao) #para chamar metodo da classe pai
        
class Guarda(NPC):
    def __init__(self, nome, time):
        self.forca = 100
        self.municao = 20
        super().__init__(nome, time, self.forca, self.municao)
    
class Elite(NPC):
    def __init__(self, nome, time):
        self.forca = 300
        self.municao = 500
        super().__init__(nome, time, self.forca, self.municao)
    
    def inf(self):
        super().info()

s1 = Guarda("Olhudo", 1) 
s2 = Soldado("Zezin", 1)
s3 = Elite("LezadoValeth", 1)
s4 = Guarda("AlmaNegra", 2)
s5 = Soldado("Faca na Pedra", 2)
s6 = Elite("Ninjado", 2)

s1.info()
s2.info()
s3.inf()
s4.info()
s5.info()
s6.inf()



    







