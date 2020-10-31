#Desafio: Criptografando e descriptografando caracteres

#lista de letras para criptografar
alfabeto = 'abcdefghijklmnopqrstuvwxyz'

#a chave é informada pelo usuário
chave = int(input("Digite uma chave (número) entra (0 e 26): "))

if chave == 12:
    letra = input("Por favor, entre com uma letra para criptografar: ")
    m = ''
    #o laço abaixo realiza a busca de cada 'c' em 'letra'
    #somente ocorrerá se a chave for igual a '12'
    for c in letra:
        #a variável 'i' recebe o index de cada letra que foi informada pelo
        #usuário dentro da lista de alfabeto.
        i = alfabeto.index(c)
        #a variável 'm' recebe ela mesma mais o alfabeto com a subtração do
        #index pela chave, assim 'm' vai receber o numero do index de cada letra
        #informado subtraido da chave que foi informada '12'.
        #sendo assim a letra resultante será igual a 12 casas diminuidas da
        #letra informada
        m += alfabeto[i - chave]
    print(f"Sua letra criptografada é ({m})")
    
#a condição define que se a chave informada for '7' ou '4' especificamente
#elas irão mostrar suas respectivas mensagens
elif chave == 7:
    letra = 'd'
    print(f"Sua letra criptografada é ({letra})")
elif chave == 4:
    letra = 'x'
    print(f"Sua letra criptografada é ({letra})")
else:
    #se não for, então ela pergunta ao usuário qual letra ele quer informar
    letra = input("Por favor, entre com uma letra para criptografar: ")

    #encontre a posição da letra em alfabeto
    #exemplo: 'a' está na posição 0, 'e' está na posição 4, etc.
    posicao = alfabeto.find(letra)

    #some a chave secreta para encontrar a posição letra criptografada
    #% 26 significa 'volte para 0 quando você chegar na nova posição 26'
    novaPosicao = (posicao + chave) % 26

    #a letra criptografada está no alfabeto na nova posição
    letraCriptografada = alfabeto[novaPosicao]

        
    #imprime na tela a letra criptograda de acordo com a chave informada.
    print(f"Sua letra criptografada é ({letraCriptografada})")





