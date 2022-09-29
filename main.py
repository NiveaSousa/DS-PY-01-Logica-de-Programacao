import random

moveis = ['Marta','Gustavo', 'Antônio', 'Joana', 'Rodrigo', 'Teodoro', 'Cristina',
'Benício', 'Artur', 'Conrado', 'Betânia', 'Estevan', 'Gabriele', 'Vicente', 'Vitório']

palavra = random.choice(moveis)
palavra = palavra.upper()

linha = len(palavra)*'_'
print('Adivinhe a Palavra:\nCategoria: Nome de pessoa\nSe a palavra tem até 5 letras, você tem 4 palpites, caso tenha mais, você tem 6. \nBoa sorte')
print(linha)

if len(palavra)<=5:
    nova_linha = linha
    for i in range (3):
        guess = input('Digite uma letra\n').upper()
        if guess in palavra:
            canto = palavra.find(guess)
            resto = palavra[canto+1:]
            if guess in resto:
                onde = resto.find(guess)
                dif = len(palavra)-len(resto)
                nova_linha = nova_linha[:canto] + guess + nova_linha[(canto+1):(onde+dif)]+guess+ nova_linha[(onde+dif+1):]
            else:
                nova_linha = nova_linha[:canto] + guess + nova_linha[(canto+1):]
            print(nova_linha)
        else:
            print('Não faz parte da palavra')
            
    else:
        guess = input('Ultima tentativa. Descubra a palavra\n').upper()
        if guess == palavra:
            print(f'Parabéns! Você acertou o nome {palavra}')
        else:
            print('Uma pena, você não acertou')


else:
    nova_linha = linha
    for i in range(5):
        guess = input('Digite uma letra\n').upper()
        if guess in palavra:
            canto = palavra.find(guess)
            resto = palavra[canto+1:]
            if guess in resto:
                onde = resto.find(guess)
                dif = len(palavra)-len(resto)
                nova_linha = nova_linha[:canto] + guess + nova_linha[(canto+1):(onde+dif)]+guess+ nova_linha[(onde+dif+1):]
            else:
                nova_linha = nova_linha[:canto] + guess + nova_linha[(canto+1):]
            print(nova_linha)
            
        else:
            print('Não faz parte da palavra\n')
    else:
        guess = input('Ultima tentativa. Descubra a palavra\n').upper()
        if guess == palavra:
            print(f'Parabéns! Você acertou o nome {palavra}')
        else:
            print('Uma pena, você não acertou')

