#Desafio: Criptografando e descriptografando mensagens

#lista de letras para criptografar
alfabeto = 'abcdefghijklmnopqrstuvwxyz'

#capture a mensagem do usuário
mensagem = input("Por favor, entre com a mensagem a ser criptografada: ").lower()

mensagemCriptografada = ''

#captura a chave secreta
chave = int(input("Digite uma chave (número) entra (0 e 26): "))

#percorra cada carctere na mensagem
for m in mensagem:
    if m in alfabeto:
        #encontre a posição da letra em alfabeto
        #exemplo: 'a' está na posição 0, 'e' está na posição 4, etc.
        posicao = alfabeto.find(m)

        #some a chave secreta para encontrar a posição letra criptografada
        #% 26 significa 'volte para 0 quando você chegar na nova posição 26'
        novaPosicao = (posicao + chave) % 26

        #acrescenta a letra descriptografada à mensagem
        #a letra criptografada está no alfabeto na nova posição
        mensagemCriptografada += alfabeto[novaPosicao]
        
    else:
        #alguns caracteres (po exempo '?') não está no alfabeto,
        # então simlesmente adicione a letra criptografada à mensagem
        mensagemCriptografada += m
        
print(f"Sua mensagem criptografada é ({mensagemCriptografada})")
