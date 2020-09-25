#Questão 05

x = int(input("Digite o 1º número: "))
y = int(input("Digite o 2º número: "))

def primo(x):
    fator = 2
    while x % fator != 0 and fator <= x/2:
        fator += 1
    if x % fator == 0:
        return False
    else:
        return True

for n in range(x, y+1):
    if primo(n):
        print(n,'É primo!')



        
   





