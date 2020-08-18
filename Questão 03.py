#Questão 03

#Solicita ao usuário um tempo em segundos de um evento.
seg = int(input("Escreva um tempo de duração de um evento em uma fábrica: "))

#A variavel dias recebe o resultado da divisão inteira entre o segundo informado
#e o valor de segundos que correponde a um dia.
dias = seg // 86400
#A variável abaixo recebe o resto da divisão entre o segundo informado
#e o valor de segundos que corresponde a um dia.
segrestante = seg % 86400
#A variável abaixo recebe o resultado da divisão inteira entre a variável (segrestante)
#e o valor de segundos que corresponde a uma hora.
horas = segrestante // 3600
#A variável abaixo recebe o resto da divisão entre elas mesma com o valor de
#segundos que corresponde a uma hora.
segrestante = segrestante % 3600
#A variável abaixo recebe o resultado da divisão inteira entre a variável(segrestante)
#e o valor de minutos que correponde a um hora.
minutos = segrestante // 60
#A variável abaixo recebe o resto da divisão entre elas mesma com o valor de
#minutos que corresponde a uma hora.
segrestante = segrestante % 60

#Imprimi (mostra) na tela o formato da hora gerado partir do segundo informado.
print(f'O valor informado corresponde em horas {horas}:{minutos}:{segrestante}')
