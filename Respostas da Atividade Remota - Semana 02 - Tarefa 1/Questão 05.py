#Questão 05

#Solicita ao usuário o valor de uma compra.
compra = float(input("Digite o valor da compra realizada: "))
#A variável abaixo recebe o resultado da fórmula abaixo com duas casas decimais.
desconto9 = round((9 / 100) * compra, 2)
#A variável abaixo recebe o valor com 9% de desconto.
valorcomdesconto =(compra - desconto9)
#A variável abaixo recebe o valor dividido em 5 vezes sem juros e descontos.
prestacao5 = round(compra / 5, 2)
#A variável abaixo recebe o resultado da fórmula da prestação de 10 parcelas.
parcel = compra/10
#A variável abaixo recebe o valor divido em 10 vezes acrescidos de 17% de juros.
prestacao10 = round((17 / 100 * parcel) + parcel, 2)

#Imprimi (mostra) para o usuário as opções de pagamento a vista com 9% de desconto.
#dividido em 5 vezes sem juros e descontos.
#e divido em 10 vezes com 17% de juros acrescidos.
print(f'O valor para pagamento a vista com desconto de 9% é R$ {valorcomdesconto}', end='')
print(f'\nO Valor da prestação para pagamento em 5 vezes, sem desconto nem juros é R$ {prestacao5}', end='')
print(f'\nO Valor da prestação para pagamento em 10 vezes, com 17% de juros é R$ {prestacao10}', end='')
