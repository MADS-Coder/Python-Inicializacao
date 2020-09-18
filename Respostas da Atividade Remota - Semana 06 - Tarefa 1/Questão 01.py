#Questão 01

deposito_inicial = int(input("Qual o depósito inicial?: "))
taxa_juros_anual = float(input("Informe a taxa de juros: "))

ano = maior = menor = 0
dobro = deposito_inicial*2

while ano < deposito_inicial:
    ano += 1
    if ano == 1:
        maior = menor = ano
        tx_anual = ((taxa_juros_anual / 100) * deposito_inicial)
        valor = deposito_inicial + tx_anual              
    else:
        tx_anual = ((taxa_juros_anual / 100) * valor)
        valor = round(valor + tx_anual, 2)
        if valor >= deposito_inicial and valor <= dobro+tx_anual:
            if ano > maior:
                maior = ano
print(f'O valor acumulado irá dobrar-se em {maior} anos.')


  
        
  


     
        
        
        
     
        
        


    



        
