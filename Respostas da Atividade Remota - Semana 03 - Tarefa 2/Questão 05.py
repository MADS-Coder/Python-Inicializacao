#Questão 05

caractere = input('Informe alguma caractere, seja letra, número ou símbolos ')

if caractere in 'aeiou':
    print('O caractere digitado é uma VOGAL.')

elif caractere in 'ABCDEFGHIJKLMNOPQRSTUVWXYZbcdfghjklmnpqrstvwxyz':
    print('O caractere digitado é uma CONSOANTE.')

elif caractere in '^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ' or caractere in '(!@#$%^&*()[]{};:,./<>?\|`~-=_+"'')':
    print('O caractere digitado é um SÍMBOLO.')

#(!@#$%^&*()[]{};:,./<>?\|`~-=_+"'')
    

else:
    print('O caractere digitado é um NÚMERO.')
