#Questão 01

lista = []
def comprimento(c):
    cont = 1
    lista.append(c)
    while True:
        c = int(input("Escreva um número, (ZERO) para encerrar: "))
        if c == 0:
            break
        else:
            lista.append(c)
            cont += 1
    return cont

def inverter(i):
    invertidos = lista
    invertidos = lista[::-1]
    return invertidos

def minimo(mi):
    men = 0
    for c in range(0, len(lista)):
        if c == 0:
            men = lista[c]
        else:
            if lista[c] < men:
                men = lista[c]
    return men

def maximo(ma):
    mai = 0
    for c in range(0, len(lista)):
        if c == 0:
            mai = lista[c]
        else:
            if lista[c] > mai:
                mai = lista[c]
    return mai

def soma(s):
    som = 0
    for s in lista:
        som += s
    return som
    
def main():
    num = int(input("Escreva um número, (ZERO) para encerrar: "))
    compri = comprimento(num)
    invertido = inverter(num)
    menor = minimo(num)
    maior = maximo(num)
    somat = soma(num)
    print(lista)
    print(f'A lista possui {compri} itens.')
    print(f'A lista invertida fica {invertido}.')
    print(f'O menor valor da lista é {menor}.')
    print(f'O maior valor da lista é {maior}.')
    print(f'A somda dos números que compõe a lista é {somat}.')


if __name__=='__main__':
    main()
