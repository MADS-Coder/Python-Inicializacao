#Questão 05

def num(a, b, c):
    if a < b < c:
        return a, b, c
    if a < c < b:
        return a, c, b
    if b < a < c:
        return b, a, c
    if b < c < a:
        return b, c, a
    if c < a < b:
        return c, a, b
    if c < b < a:
        return c, b, a
    if a == b or a == c or b == c:
        return 'Inválido'

def main():
    n1 = int(input('Informe um número: '))
    n2 = int(input('Informe um número: '))
    n3 = int(input('Informe um número: '))

    resultado = num(n1, n2, n3)

    print(f'O resultado em ordem crescente é {resultado}.')


if __name__=='__main__':
    main()
