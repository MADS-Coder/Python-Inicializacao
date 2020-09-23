#Questão 03

populacao_B = int(input("Informe a população do País B: "))
populacao_A = int(input("Informe a população do País A: "))

A = (0.02*populacao_A)+populacao_A
B = (0.03*populacao_B)+populacao_B
ano = 0
while True:
    ano += 1
    while A > B:
        A = (0.02*A)+A
        B = (0.03*B)+B
        break
    else:  
        A = (0.03*populacao_A)+populacao_A
        B = (0.02*populacao_B)+populacao_B
        while A < B:
            ano += 1
            A = (0.03*A)+A
            B = (0.02*B)+B
        else:
            break
print(f'Irá ultrapassar com {ano} anos.')





