#Questão 02

lista = []
def valor(n):
    cont = 1
    lista.append(n)
    while True:
        n = int(input("Escreva um número, (ZERO) para encerrar: "))
        if n == 0:
            break
        else:
            lista.append(n)
            cont += 1
    valor = int(input("Digite um valor que compõe a lista para saber quantas ocorrências aparecem: "))
    print(f'A lista é {lista}.')
    print(f'A quantidade de vezes em que o numero {valor} apareceu na lista, ', end='')
    ocorrencia = lista.count(valor)
    return ocorrencia

def main():
    num = int(input("Escreva um número, (ZERO) para encerrar: "))
    res = valor(num)
    print(f'foi {res} vezes.')


if __name__=='__main__':
    main()
