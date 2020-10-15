#Questão 02

agendas = [] 
pessoa = {}
agenda = int(input('Qual o tamanho da agenda?: '))
for c in range(1, agenda+1):
    pessoa.clear()
    pessoa['Nome'] = str(input("Qual o nome: ")).strip()
    pessoa['Cidade'] = str(input("Informe a cidade: ")).strip()
    pessoa['UF'] = str(input("Qual UF: ")).upper().strip()
    pessoa['Tel'] = input("Informe o telefone: ").strip()
    agendas.append(pessoa.copy())
for p in agendas:
    u = p["UF"]
    c = p["Cidade"]
    uc = c+"("+u+")"
    print(f'{p["Nome"]:<20}{uc:<30}{p["Tel"]}', end='')
    print()

