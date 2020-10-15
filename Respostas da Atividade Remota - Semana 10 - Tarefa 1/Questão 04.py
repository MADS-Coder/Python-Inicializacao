#Questão 04

vogal = {}
vo = []
vogal["Texto"] = str(input("Digite um texto para saber quantoas vogais ele tem: ")).strip().lower()
for k, v in vogal.items():
    for letra in v:
        if letra in 'aeiouáàâãéêèîíìôóòõúùû':
            vo.append(letra)
            A = vo.count('a')+vo.count('á')+vo.count('à')+vo.count('â')+vo.count('ã')     
            E = vo.count('e')+vo.count('é')+vo.count('è')+vo.count('ê')
            I = vo.count('i')+vo.count('í')+vo.count('ì')+vo.count('î')
            O = vo.count('o')+vo.count('ó')+vo.count('ò')+vo.count('ô')+vo.count('õ')
            U = vo.count('u')+vo.count('ú')+vo.count('ù')+vo.count('û')
print(f'A: {A}\nE: {E}\nI: {I}\nO: {O}\nU: {U}')


