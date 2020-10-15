#Questão 05

lista = []
dados = {}
alunos = {}
lista_alunos = []
cont = c = 0
matricula = ""
def ler():
    global matricula
    matricula = input("Informe a matricula do aluno: ")
    return matricula

def matriculas():
    while ler() != "":
        dados.clear()
        dados["nome"] = str(input("Digite o nome do aluno: ")).strip()
        dados["matricula"] = matricula
        dados["n1"] = float(input("Digite a 1º nota: "))
        dados["n2"] = float(input("Digite a 2º nota: "))
        s = dados["n1"] + dados["n2"]
        dados["media"] = round(s/2, 1)
        lista.append(dados.copy())
    return lista
m = matriculas()

while True:
    chave = str(input("Informe a matricula para buscar o nome e media do aluno: "))
    for p in lista:
        if str(chave) == p['matricula']:
            alunos.clear()
            alunos["nomes"] = p['nome']
            alunos["medias"] = p['media']
            lista_alunos.append(alunos.copy())
            cont += 1
    if chave == "":
        break
    
for n in lista_alunos:
    print(f'{n["nomes"]}: {n["medias"]}')

