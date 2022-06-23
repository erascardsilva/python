"""
        Python
        Jogo adivinhar palavra
        Erasmo Cardoso
"""

palavra = input('  Digite a palavra  :  ')
digitadas = []
chances = 5

while True:
    if chances <= 0:
        print('Voce perdeu!!!!!')
        break

    letra = input('Digite uma letra  :  ')

    if len(letra) > 1:
        print('Digite apenas letras!!!!!!')
        continue

    digitadas.append(letra)

    if letra in palavra:
        print(f'A  letra "{letra}" existe na palavra')

    else:
        print(f'A letra "{letra}" não existe na palavra')
        digitadas.pop()

    secretas_temporario = ''
    for letra_secreta in palavra:
        if letra_secreta in digitadas:
            secretas_temporario += letra_secreta
        else:
            secretas_temporario += '*'
    print(secretas_temporario)

    if secretas_temporario == palavra:
        print('Voce acertou')
        break

    else:
        print(f'A palavra secreta esta assim  : "{secretas_temporario}"  ')

    if letra not in palavra:
        chances -= 1
        print(f'Voce ainda tem {chances} chances')
