#Questão 02 - (e)

#Solicita os dados pelo usuário
altura = float(input("Informe a altura da sala em (m): "))
compri = float(input("Informe o comprimento da sala em (m): "))
largura = float(input("Informe a largura da sala em (m): "))

#Calcula a área do piso da sala
areap = round(largura * compri, 2)

#Calcula o volume da sala
volume = round(largura * compri * altura, 2)

#Calcula a área das paredes da sala
areapa = round((2 * altura * largura) + (2 * altura * compri), 2)

#Imprimi a Área do piso da sala, o volume da sala e a área das paredes da sala
print(f"A Área do piso da sala é de {areap} metros, \nO Volume da sala é de {volume} metros,\nE a Área das paredes é de {areapa} metros.")
