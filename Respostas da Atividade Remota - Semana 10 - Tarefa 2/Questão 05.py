#Questão 05
agenda = {}
def incluirNovoNome():#1
    nome = input("Digite o nome: ")
    telefone = [input("Digite o telefone: ")]
    nomes = (nome, telefone)
    agenda[nome] = nomes
    
def ler(nome):
    nome, telefone = agenda[nome]
    return nome, telefone

def incluirTelefone(nome):#2
    nome, telefone = ler(nome)
    aux = input(f'Nome (atual:{nome}): ')
    if aux != '':
        nome = aux
    aux = input(f"Telefone (atual: {telefone}): ")
    if aux != '':
        nova = input(f"Incluir telefone? (S, N): ")[0].upper() == 'S'
        if nova:
            agenda[nome][1].append(aux)
            print('Telefone incluído com sucesso.')

    agenda[nome] = (nome, telefone)
    
def excluirNome(nome):#3
    nome, _ = ler(nome)
    confirma = input(f'Deseja realmente apagar {telefone}? (S, N): ')[0].upper() == 'S'
    if confirma:
        del agenda[nome]
        
def excluirTelefone(nome):#4
    _, telefone = ler(nome)
    confirma = input(f'Deseja realmente apagar {nome}? (S, N): ')[0].upper() == 'S'
    if confirma:
        del agenda[nome]
        
def listar_Agenda():#5
    qtd = 0
    for nome in agenda:
        nome, telefone = ler(nome)
        print('-'*30)
        print(f'Código do Nome: {nome}')
        print(f"Nome: {nome}")
        print(f"Telefone: {telefone}")
        qtd += 1
    if qtd == 0:
        print('<<< Nenhum dado para mostrar >>>')
              
def menu():
    while True:
        print('1 - Incluir Novo Nome')
        print('2 - Incluir Telefone')
        print('3 - Excluir Telefone')
        print('4 - Excluir Nome')
        print('5 - Mostrar Agenda')
        print('0 - Fim do Programa')
        print('='*30)
        opcao = int(input("Digite sua opção: "))
        if opcao in (1, 2, 3, 4, 5, 0):
            return opcao
        else:
            print('Opção Inválida')
def main():
    while True:
        op = menu()
        if op == 1: #Create
            incluirNovoNome()
        elif op == 2: #Update
            nome = input('Nome para carregar: ')
            if nome in agenda:
                incluirTelefone(nome)
            elif nome not in agenda:
                print(f'Nome não existe com o nome {nome}')
                res = input("Deseja incluí-lo? (S, N): ")[0].upper() == 'S'
                if res:
                    incluirNovoNome()
        elif op == 3: #Delete
            nome = input('Nome para Remover: ')
            if nome in agenda:
                excluirTelefone(nome)
            else:
                print(f'Código não existe com o nome {nome}')
        elif op == 4: #Delete
            telefone = input('Telefone para Remover: ')
            if telefone in agenda:
                excluirTelefone(nome)
            else:
                print(f'Código não existe com o telefone {telefone}')
        elif op == 5: #Listar todos
            listar_Agenda()
        elif op == 0:
            print('Fim do programa.')
            break
        else:
            pass
if __name__=='__main__':
    main()
            
            
            
