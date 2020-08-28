#DESAFIO QUIZ
#Quiz de múltipla escolha

print('=' * 45)
print('     VAMOS VER SE VOCÊ GOSTA DE HISTÓRIA       ')
print('=' * 45)
print('''Em qual país ocorreu a Batalha da Normandia?
a - Brasil
b - Irlanda
c - Piauí
d - França
e - Eslováquia''')
pais = input('Qual sua resposta? ').lower()

if pais == 'd':
    print(':):):):):):) Você é um historiador....PARABENSSSSSSSSSSS')
elif pais != 'd':
    while pais != 'd':
        print('Alternativa incorreta...Por favor tente novamente.')
        pais = input('Qual sua resposta? ').lower()
        if pais == 'd':
            print(':):):):):):) Você é um historiador....PARABENSSSSSSSSSSS')
