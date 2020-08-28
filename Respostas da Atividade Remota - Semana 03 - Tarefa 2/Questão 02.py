#Questão 02

dados = input('Informe uma letra, número ou caractere ')

if dados in 'aeiou':
    print('O caractere digitado é uma vogal, portanto é VERDADEIRO.')

elif dados in 'ABCDEFGHIJKLMNOPQRSTUVWXYZbcdfghjklmnpqrstvwxyz':
    print('O caractere digitado é uma consoante, portanto é VERDADEIRO.')
    
else:
    print('O caractere digitado não é vogal ou consoante, portanto é FALSO.')
