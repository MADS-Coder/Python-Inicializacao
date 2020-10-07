#Questão 02

T = []

def temp():
    for pos in range(1,3):
        temperatura = float(input("Digite uma temperatura: "))
        escala = input('Escala?: ').upper()[0]
        T.append(temperatura)
        T.append(escala)  
    return T

def conversão():
    #Se forem as mesmas escalas ele retorna a maior temperatura entre elas.
    if T[1] == 'C' and T[3] == 'C':
        if T[0] >= T[2]:
            maior = T[0]
            e = 'C'
        else:
            maior = T[2]
            e = 'C'
    elif T[1] == 'F' and T[3] == 'F':
        if T[0] >= T[2]:
            maior = T[0]
            e = 'F'
        else:
            maior = T[2]
            e = 'F'
            
    #Se não forem inguais, ele vai fazer as conversões de acordo com as condições.
    else:
        if T[1] == 'C' and T[3] == 'F':
            if T[0] > T[2]:
                F = (T[0] *(9/5)) + 32
                maior = F
                e = 'F'
            else:
                maior = T[2]
                e = 'F'
        elif T[1] == 'F' and T[3] == 'C':
            if T[2] < T[0]:
                C = (T[0]-32)*(5/9)
                maior = C
                e = 'C'
            else:
                maior = T[2]
                e = 'C'
    t = []
    t.append(maior)
    t.append(e)
    E = tuple(t)
    return E


def soma():
    if T[1] == 'C' and T[3] == 'C':
        s = round(T[0]+T[2], 4)
        e = 'C'
    elif T[1] == 'F' and T[3] == 'F':
        s = round(T[0]+T[2], 4)
        e = 'F'
    else:
        if T[1] == 'C' and T[3] == 'F':
            F = (T[0] *(9/5)) + 32
            s = round(F+T[2], 4)
            e = 'F'
        elif T[1] == 'F' and T[3] == 'C':
            C = (T[0]-32)*(5/9)
            s = round(C+T[2], 4)
            e = 'C'
    t = []
    t.append(s)
    t.append(e)
    E = tuple(t)
    
    return E

def main():
    temperatura = temp()
    conversao = conversão()
    resultado = soma()

    print(resultado)

if __name__=='__main__':
    main()
    
    
    













 


