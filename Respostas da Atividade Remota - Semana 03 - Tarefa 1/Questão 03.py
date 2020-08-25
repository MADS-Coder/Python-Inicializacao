#Questão 03

print('-='*20)
print(f'{"SINAIS DE TRÂNSITO":^40}')
print('-='*20)
print('''
[V] Verde
[A] Amarelo
[E] Vermelho
''')
sinal = str(input('Escolha uma cor de sinal de trânsito\n'))

if sinal in 'Vv' and 'Verdeverde':
    print('Muito bem. SIGA')
    
elif sinal in 'Aa' and 'Amareloamarelo':
    print('ATENÇÃO')
    
else:
    print('Sinal fechado por favor PARE')
