#Questão 02


def par(a, b, c):

    if a and b % 2 != 1:
        return 'tem 2 dítos pares.'
    if b and c % 2 != 1:
        return 'tem 2 dígitos pares.'
    if a and c % 2 != 1:
        return 'tem 2 dígitos pares.'
    
def par1(a, b, c):
    
    if a % 2 == 0:
        return 'tem 1 dígito par.'
    if b % 2 == 0:
        return 'tem 1 dígito par.'
    if c % 2 == 0:
        return 'tem 1 dígito par.'

def main():
    num = int(input('Informe um número entre [100] e [999]: '))
    n1 = num // 100 % 10
    n2 = num // 10 % 10
    n3 = num // 1 % 10

    
    
    res = par(n1, n2, n3)
    res1 = par1(n1, n2, n3)
    



if __name__=='__main__':
    main()
