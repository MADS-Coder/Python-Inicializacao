#Questão 04

def n_sorte(n):
    n1 = n // 1 % 10
    n2 = n // 10 % 10
    n3 = n // 100 % 10
    n4 = n // 1000 % 10
    n5 = n // 10000 % 10
    n6 = n // 100000 % 10
    n7 = n // 1000000 % 10
    n8 = n // 10000000 % 10
    numero_sorte = n8+n7+n6+n5+n4+n3+n2+n1

    return numero_sorte

def main():
    dt_nasc = int(input("Escreva sua data de nascimento [ddmmaaaa]: "))
    sorte = n_sorte(dt_nasc)
    print(f'Seu número da sorte é {sorte}.')
    
if __name__=='__main__':
    main()
