#Questão 02

mes = []
e = []
C = []
soma = 0
for m in range(1, 13):
    if m == 1:
        m = 'Janeiro'
    elif m == 2:
        m = 'Fevereiro'
    elif m == 3:
        m = 'Março'
    elif m == 4:
        m = 'Abril'
    elif m == 5:
        m = 'Maio'
    elif m == 6:
        m = 'Junho'
    elif m == 7:
        m = 'Julho'
    elif m == 8:
        m = 'Agosto'
    elif m == 9:
        m = 'Setembro'
    elif m == 10:
        m = 'Outubro'
    elif m == 11:
        m = 'Novembro'
    elif m == 12:
        m = 'Dezembro'      
    temperatura = float(input(f'Digite a temperatura do mes de {m}: '))
    escala = input("Qual a escala, (C, F OU K): ").upper()[0]
    if escala == 'C':
        T = round(temperatura + 273.15, 2)
    if escala == 'F':
        T = round(((temperatura-32)/1.800) + 273.15, 2)
    if escala == 'K':
        T = temperatura
    mes.append(m)
    e.append(T)
    soma = round(soma + T, 2)
media = round(soma/12, 2)
print(f'TEMPERATURA MÉDIA ANUAL\n{media}K')
print('TEMPERATURAS ACIMA DA MÉDIA ANUAL:')
for i,j in zip(mes, e):
    C.append(i)
    C.append(j)
    for n in range(1, 13):
        if j > media:
            print(f'{i}: {j}K')
            break
   





    
    
    
    





 


