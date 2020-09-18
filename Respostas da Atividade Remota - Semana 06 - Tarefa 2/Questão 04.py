#Questão 04

print('-='*20)
print(f'{"CARDÁPIO CASA LANCHES":^40}')
print('-='*20)
print('''CÓDIGO    PRODUTO            PREÇO (R$)
  [H]   Hamburguer              5.50
  [C]   Cheeseburguer           6.80
  [M]   Misto Quente            4.50
  [A]   Americano               7.00
  [Q]   Queijo Prato            4.00
  [X]   PARA TOTAL DA CONTA\n''')
codigo = str(input("Digite o código do lanche desejado: ")).upper()[0]
cont = soma = preco = 0
while True:
    if codigo == 'H':
        preco = 5.50
    elif codigo == 'C':
        preco = 6.80
    elif codigo == 'M':
        preco = 4.50
    elif codigo == 'A':
        preco = 7.00
    elif codigo == 'Q':
        preco = 4.00
    elif codigo == 'X':
        break
    elif codigo not in 'HhCcMmAaQqXx':
        print("Opção inválida")

    soma += preco
    codigo = str(input("Digite o código do lanche desejado: ")).upper()[0]

print(f'\nO valor total do pedido é R$ {soma:.2f}')
