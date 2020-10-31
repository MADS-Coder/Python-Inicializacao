#Desafio: Calculadora do amor

print("Calculadora do amor")
print("<3 "*7)

#solicita ao usuario o nome de duas pessoas
#converte os nomes para minúsculos e tira os espaços
nomes = input("Digite o nome de 2 pessoas: ").strip().lower()

#atribui o valor zero para a variável placar
placar = 0

#o laço de repetição realiza a busca de cada letra nos nomes.
for letra in nomes:
    #a condição define que se as letras no loop do laço estiver nas vogais
    #o placar que é zero recebe ele mesmo mais 5 pontos.
    if letra in "aeiou":
        placar += 5
    #a condição define que se as letras no loop do laço estiver na palavra amor
    #o placar que é zero recebe ele mesmo mais 10 pontos.    
    if letra in "amor":
        placar += 10

#imprime uma mensagem com o valor do placar de acordo com o resultado
#das condições informadas
print(f"Seu placar de compatibilidade : {placar}")

#estrutura de condição para exibir uma mensagem personalizada
#caso o placar seja menor que dez, então imprime a mensagem
if placar < 10:
    print("Esqueça esta pessoas! Nunca vai dar certo!")
    
#caso não seja, ele imprime a mensagem abaixo
else:
    print("Vocês terão um relacionamento muito intenso! <3")


