#Questão 01

tartaruga = int(input("Quantos metros a tartaruga sai a frente da lebre?: "))
while True:
    tempo = (((tartaruga//500)*60)+tartaruga)//10
    print(f'A lebre alcançará a tartaruga em {tempo} minutos.')
    print("Quer continuar? [s/n] ", end=" ")
    resposta = str(input()).lower()
    if resposta not in 'NnSsnaosimNAOSIM':
        print("Por favo digite so [s/n]. Quer continuar?", end=" ")
        resposta = str(input()).lower()
        tartaruga = int(input("Quantos metros a tartaruga sai a frente da lebre?: "))
    elif resposta in 'Nn' or resposta == 'nao':
        break
    else:
        tartaruga = int(input("Quantos metros a tartaruga sai a frente da lebre?: "))
          
print("Obrigado por ter participado deste teste :)!!")   
