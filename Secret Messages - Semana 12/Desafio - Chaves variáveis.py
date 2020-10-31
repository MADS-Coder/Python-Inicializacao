#Desafio: Chaves variáveis

#lista de letras para criptografar
alfabeto = 'abcdefghijklmnopqrstuvwxyz'

#a chave é informada pelo usuário
chave = int(input("Digite uma chave (número) entra (0 e 26): "))

letra = input("Por favor, entre com uma letra para criptografar: ")

#encontre a posição da letra em alfabeto
#exemplo: 'a' está na posição 0, 'e' está na posição 4, etc.
posicao = alfabeto.find(letra)

#some a chave secreta para encontrar a posição letra criptografada
#% 26 significa 'volte para 0 quando você chegar na nova posição 26'
novaPosicao = (posicao + chave) % 26

#a letra criptografada está no alfabeto na nova posição
letraCriptografada = alfabeto[novaPosicao]

print(f"Sua letra criptografada é ({letraCriptografada})")
