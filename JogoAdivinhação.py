'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
print ('Python - Aula18: Jogo de Adivinhação')

import random
import os

erros = 0
sorteado = random.randrange(0, 100)
jogador = int(input("Digite o seu número: "))

while(sorteado != jogador):
    os.system("clear")
    if(sorteado>jogador):
        print("ERRO, o numero é maior")
    elif(sorteado < jogador):
        print("ERRO, o numero é menor")
    erros+=1
    jogador=int(input("Digite o seu numero: "))
print("Numero " + str(jogador) + ", voce acertou em " + str(erros + 1) + " tentativas")
    
    

