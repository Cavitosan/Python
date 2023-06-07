import random

palavras = ['banana', 'morango', 'abacaxi', 'laranja', 'pinha']

palavra = random.choice(palavras)

vidas = 6
letras_acertadas = ['_'] * len(palavra)
letras_erradas = []

while True:
    print('Palavra: ', ' '.join(letras_acertadas))
    print('Vidas restantes: ', vidas)
    print('Letras erradas: ', ' '.join(letras_erradas))

    palpite = input('Digite uma letra: ').lower()

    if len(palpite) != 1:
        print("Digite apenas uma letra por vez!")
        continue

    if palpite in letras_acertadas or palpite in letras_erradas:
        print("Voce já tentou essa letra antes!!")
        continue

    if palpite in palavra:
        for i in range(len(palavra)):
            if palavra[i] == palpite:
                letras_acertadas[i] = palpite
    else:
        letras_erradas.append(palpite)
        vidas -= 1

    if '_' not in letras_acertadas:
        print('Voce ganhou!')
        break
    elif vidas == 0:
        print('Voce perdeu! A palavra era: ', palavra)
        break
