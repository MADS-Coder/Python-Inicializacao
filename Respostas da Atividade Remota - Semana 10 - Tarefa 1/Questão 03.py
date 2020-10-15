#Questão 03

agendas = [] 
pessoa = {}
for c in range(1, 21):
    pessoa.clear()
    pessoa['Nome'] = str(input("Qual o nome: ")).strip()
    pessoa['Idade'] = int(input("Informe a idade: ")).strip()
    pessoa['CPF'] = input("Qual o seu CPF: ").strip()
    agendas.append(pessoa.copy())
print('========== MAIORES DE 18 ANOS ==========')
for p in agendas:
    if p["Idade"] >= 18:
        print(f'{p["Nome"]};{p["Idade"]};{p["CPF"]}', end='')
        print()
print('========== MENORES DE 18 ANOS ==========')
for v in agendas:
    pessoa.clear()
    if v["Idade"] < 18:
        print(f'{v["Nome"]};{v["Idade"]};{v["CPF"]}', end='')
        print()
