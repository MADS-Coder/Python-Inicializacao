#Questão 04

nome = str(input("Digite qualquer palavra: "))
caractere = len(nome)

if 0 < len(nome) > 9:
    print(f'O nome {nome} contem {caractere} caractere é maior que [9], \nportanto é FALSO.')

else:
    print(f'O nome {nome} contem {caractere} caractere está entre [0] e [9], \nportanto é VERDADEIRO.')
