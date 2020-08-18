#Questão 02

#Solicita ao usuário que informe um caractere.
carac = input("Informe um caractere[Nº ou LETRA] para saber seu código numérico: ")

#Retorna ao código Unicode do caractere informado.
cod = ord(carac)

#Imprimi (mostra) ao usuário o código unicode do caractere informado.
print(f'O código númerico do caractere {carac} informado é {cod}')
