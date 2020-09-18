#Questão 03

quant = maior = menor = 0
num = int(input("Escreva um número positivo termiando em ZERO[0]. Digite [999] para finalizar: "))
while True:
    quant += 1
    if num == 0:
        break
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    num = int(input("Escreva um número positivo termiando em ZERO[0]. Digite [999] para finalizar: "))

if maior == 0 and menor == 0:
    print("Nenhum numero digitado")
else:    
    print(f'O maior {maior} e o menor {menor}.')
    

   

