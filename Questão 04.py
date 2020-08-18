#Questão 04

#Variável contadora.
cont = 0
#Variável recebe uma lista.
lista = []
#Laço de repetição FOR onde a variável de controle (n) repetirá a quantidade correpondente no
#intervalo de (1 a 5).
for n in range(1,6):
#Solicita ao usuário um valor.
    num = int(input("Digite um valor: "))
#Adiciona na lista os valores informados pelo usuário.
    lista.append(num)
#A variável (maior) recebe da lista o maior número informado.
    maior = max(lista)
#A variável (menor) recebe da lista o menor número informado.
    menor = min(lista)
#A variável (s) recebe a soma de todos os valores dentro da lista.
    s = sum(lista)
#A variável (cont) recebe a soma da repetição do laço dele com 1,
#pois a mesma inicia com 0.
    cont += 1
#A variável (media) recebe o resultado da fórmula da média dos numeros informados. 
    media = s / cont
#Imprime (mostra) ao usuário o maior, menor e a media refente aos números informados.
print(f'O MAIOR número digitado foi {maior} \nO MENOR número digitado foi {menor} \nE a MÉDIA é {media}')
