#Questão 02 - (b)

#Solicita ao usuário três números inteiros.
a = int(input("Digite o 1 número: "))
b = int(input("Digite o 2 número: "))
c = int(input("Digite o 3 número: "))

#Calcula a média a partir das informações dadas pelo usuário.
media = round((a+b+c)/3, 2)

#Imprimi(mostra) ao usuário a média ao usuário.
print(f'A média dos números é {media}')
