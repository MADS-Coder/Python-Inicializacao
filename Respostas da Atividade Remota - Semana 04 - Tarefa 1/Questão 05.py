#Questão 05

massa = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
IMC = round(massa/altura**2, 2)

if IMC < 18.5:
    print(f'O seu IMC é {IMC}, e você está Abaixo do Peso.')
elif IMC > 18.5 and IMC < 25:
    print(f'O seu IMC é {IMC}, e você está Peso normal.')
elif IMC > 25 and IMC < 30:
    print(f'O seu IMC é {IMC}, e você está Sobrepeso.')
elif IMC > 30 and IMC < 35:
    print(f'O seu IMC é {IMC}, e você está Obeso leve.')
elif IMC > 35 and IMC < 40:
    print(f'O seu IMC é {IMC}, e você está Obeso moderado.')
elif IMC >= 40:
    print(f'O seu IMC é {IMC}, e você está Obeso mórbido.')

        
