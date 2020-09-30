#Desafio: Duplicação de hobbies

from random import *

executa  = True
adjetivos = ["maravilhoso","acima da média", "excelente",
             "um caminhão carregado de ouro", "admirável",
             "brilhante", "magnífico", "eminente","bravo"]
hobbies = ["ler", "andar de bicicleta", "programar", "ouvir musica",
           "fazer chá", "fazer caminhada", "correr","meditar",
           "fazer yoga", "cantar", "viajar", "pescar"]

print("Gerador de Cumprimentos")
print("-----------------------")

nome = input("Qual o seu nome?: ")

print('''
Menu
    c = Obter cumprimento
    a = Adicionar hobby
    d = Remover hobby
    p = Imprimir hobbies
    q = Sair
''')

while executa == True:
    menuChoice = input("\n>_").lower()
    
    if menuChoice == 'c':
        print("Aqui está o seu cumprimento", nome,":")
        print(nome, "você é", choice(adjetivos), "em", choice(hobbies))
        print("De nada!")
    elif menuChoice == 'a':
        itemToAdd = input("Adicione o hobby: ")
        if itemToAdd not in hobbies:
            hobbies.append(itemToAdd)
        else:
            print("Já consta o hobby na lista")
            
    elif menuChoice == 'd':
        itemToDelete = input("Insira o hobby a ser removido: ")
        if itemToDelete in hobbies:
            hobbies.remove(itemToDelete)
        else:
            print("O hobby não está na lista!")
    elif menuChoice == 'p':
        print(hobbies)
    elif menuChoice ==  'q':
        executa = False
    else:
        print("Insira uma opção válida!")

    
