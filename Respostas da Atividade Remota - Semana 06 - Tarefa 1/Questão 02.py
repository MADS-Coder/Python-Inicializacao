#Questão 02

soma = media = 0
cont = -1
num = int(input("Escreva um número positivo. Digite [0] para finalizar e calcular a média: "))
while True:
    cont += 1
    soma += num
    if num == 0:
        break
    else:
        num = int(input("Escreva um número positivo. Digite [0] para finalizar e calcular a média: "))
if soma == 0:
    print("Nenhum número digitado.")
else:
    media = round(soma / cont, 2)
    print(f'Você digitou {cont} números positivos, e a média sem o ZERO é {media}.')
   

        
    
    



        
