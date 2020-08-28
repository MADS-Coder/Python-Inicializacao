#Questão 04


carac = input('Informe alguma letra, número ou caractere ')

if carac in '0123456789':
    print('O caractere informado é um número que está entre 0 e 9, portanto é VERDADEIRO.')
    
elif carac in 'aeiou':
    print('O caractere informado é uma vogal, portanto é VERDADEIRO.')
    
elif carac in 'ABCDEFGHIJKLMNOPQRSTUVWXYZbcdfghjklmnpqrstvwxyz':
    print('O caractere informado é uma consoante, portanto é VERDADEIRO.')

else:
    print('O caractere informado, não é vogal, nenhum nº de 0 a 9, ou consoante,\nportanto é FALSO.')
