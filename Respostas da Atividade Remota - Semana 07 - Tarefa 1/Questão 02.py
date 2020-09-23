#Questão 02

carro = float(input("Informe o valor: "))
aumento_p_carro = (0.004*carro)+carro
poupanca_inicial = 10000
rendimento = (0.007*poupanca_inicial)+poupanca_inicial
mes = -1
while True:
    mes += 1
    aumento_p_carro = (0.004*aumento_p_carro)+aumento_p_carro
    if rendimento < aumento_p_carro:
        rendimento = (0.007*rendimento)+rendimento
    else:
        break

print(f'Em {mes} meses poderá comprar um carro a vista com as aplicações.')
