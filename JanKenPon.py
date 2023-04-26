'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import random

print("Rock, Paper, Scissors Game")
print("Enter choice \n1. Rock \n2. Paper \n3. Scissors \n")

choice = int(input("User turn: "))

while choice > 3 or choice < 1:
    choice = int(input("Enter valid input: "))

if choice == 1:
    choice_name = 'Rock'
elif choice == 2:
    choice_name = 'Paper'
else:
    choice_name = 'Scissors'

print("Your turn: ", choice_name)
print("Now its computer's turn.......")

comp_choice = random.randint(1, 3)

if comp_choice == 1:
    comp_choice_name = 'Rock'
elif comp_choice == 2:
    comp_choice_name = 'Paper'
else:
    comp_choice_name = 'Scissors'

print("Computer turn: ", comp_choice_name)
print(choice_name, " V/S ", comp_choice_name)

result = (choice - comp_choice + 3) % 3

if result == 0:
    print("TIE")
elif result == 1:
    print("You Win")
else:
    print("Computer Wins")

