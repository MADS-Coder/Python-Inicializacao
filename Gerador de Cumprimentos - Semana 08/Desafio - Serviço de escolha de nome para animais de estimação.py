#Desafio: Serviço de escolha de nome para animais de estimação

from random import *

executa  = True
femea = ["Nikita", "Neném", "Nina", "Nala", "Nanda", "Nani", "Natasha",
         "Nicole", "Nanny", "Queen", "Quindim", "Rayka", "Riana",
         "Rumba", "Rahnna", "Rosa", "Rayssa", "Rebeca", "Rubi",
         "Wally", "Willy", "Wendy", "Whisky", "White"]
macho = ["Thor", "Zeus", "Floquinho", "Sheik", "Luke", "Apolo", "Jimmy", "Bolota",
         "Nick", "Boris", "Charlie", "Eros", "Theo", "Tobby", "Barth", "Zé", "Billy",
         "Pingo", "Scott", "Totó", "Bob", "Duque", "Elvis", "Lorde", "Fred", "Toddy",
         "Sushi", "Dexter", "Pingo", "Spike", "Tom", "Brutus", "Chico", "Simba"]

print("Serviço de escolha de nome para animais de estimação")
print("----------------------------------------------------")

nome = input("De quantos nomes você precisa: ")
sexo = input("é macho ou fêmea?[M/F]: ")

print('''
Menu
    c = Obter o nome do seu animal
    a = Adicione um nome de estimação
    d = Remover um nome de estimação
    p = Imprimir os nomes do animal
    q = Sair
''')
while executa == True:
    menuChoice = input("\n>_").lower()
    if menuChoice == 'c':
        if sexo in 'Ff':
            print("Você deve chamar seu animal de estimação de", choice(femea))
            print("De nada!")
        else:
            print("Você deve chamar seu animal de estimação de", choice(macho))
            print("De nada!")
    elif menuChoice == 'a':
        itemToAdd = input("Adicione um nome de estimação: ")
        if itemToAdd not in femea:
            femea.append(itemToAdd)
            print("Nome inserido com sucesso")
        if itemToAdd not in macho:
            macho.append(itemToAdd)
        else:
            print("Já consta o nome de estimação na lista")    
    elif menuChoice == 'd':
        itemToDelete = input("Insira o nome de estimação a ser removido: ")
        if itemToDelete in femea:
            femea.remove(itemToDelete)
            print("Nome removido com sucesso")
        elif itemToDelete in macho:
            macho.remove(itemToDelete)
            print("Nome removido com sucesso")
        else:
            print("O nome de estimação não está na lista!")
    elif menuChoice == 'p':
        if sexo in 'Ff':
            print(femea)
        else:
            print(macho)
    elif menuChoice == 'q':
        executa = False
   
    else:
        print("Insira uma opção válida!")

    
