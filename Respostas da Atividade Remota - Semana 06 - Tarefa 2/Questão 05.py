#Questão 05


nota = float(input("Digite a nota do aluno entre [0 e 10]: "))
while True:
    if nota >= 8.5 and nota <= 10:
        print("O conceito do aluno é A.")
    elif nota >= 7.0 and nota <= 8.4:
        print("O conceito do aluno é B.")
    elif nota >= 5.0 and nota <= 6.9:
        print("O conceito do aluno é C.")
    elif nota >= 4 and nota <= 4.9:
        print("O conceito do aluno é D.")
    elif nota >= 0 and nota <= 3.9:
        print("O conceito do aluno é E.")
    else:
        print("Nota inválida!")       
    nota = float(input("Digite a nota do aluno entre [0 e 10]: "))
    
