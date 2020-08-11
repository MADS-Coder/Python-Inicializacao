#Questão 02 - (a)

#Solicita as informações de dia, mês e ano para o usuário
dia = int(input("Digite o número de um dia: "))
mes = int(input("Digite o número de um mês: "))
ano = int(input("Digite o número de um ano: "))

#Imprimi(mostra) ao usuário o formato da data a partir das informações dadas.
print("A data informada é {}/{:02d}/{}".format(dia, mes, ano))
