#Questão 02 - (d)

#Solicita ao usuário as informações de hora, minuto e segundos.
hora = int(input("Informe uma hora: "))
minuto = int(input("Informe quantos minutos: "))
segundo = int(input("Informe quantos segundos: "))

#Segundos referente a 24 horas.
meianoite = 86400 

#Convertendo horas para minutos.
mintotal = (hora * 60) + minuto
#Convertendo minutos para segundos referente a entrada de dados.
segtotal = (mintotal * 60) + segundo 

#Imprimi(mostra) ao usuário quantos segundos se passaram desde a ultima meia-noite.
print(f'Se passaram {segtotal} segundos desde a ultima meia-noite.')
