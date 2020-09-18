#Questão 04

def nuns(n):
    n_invertido = int(str(n)[::-1])
    return n_invertido
    
def main():
    num = int(input("Digite um número para ver a sua forma invertida: "))
    q = nuns(num)
    print(f'{q}')

if __name__=='__main__':
    main()
