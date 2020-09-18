#Questão 03



print('-='*20)
print(f'{"MENU DE OPÇÕES":^40}')
print('-='*20)
print('''[1] - Saudação
[2] - Bronca
[3] - Felicitação
[0] - Fim\n''')
opcao = int(input("Escolha uma das opções acima: "))
while True:
    if opcao == 1:
        print("Olá. Como vai?")
    elif opcao == 2:
        print("Vamos estudar mais.")
    elif opcao == 3:
        print("Meus Parabéns!")
    elif opcao != 1 and opcao != 2 and opcao != 3 and opcao != 0:
        print("Opção inválida")
    elif opcao == 0:
        print("Fim de serviço")
        break
    opcao = int(input("Escolha uma das opções acima: "))
