#Questão 04

def carrega_cidades():
    resultado = []
    populacao = int(input("Digite a quantidade de população: "))
    print(f'CIDADES COM MAIS DE {populacao} HABITANTES:')
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            for n in (1, 5558):
                if int(pop) >= populacao:
                    print(f'IBGE: {ibge} - {nome}({uf}) - POPULAÇÃO: {pop}', end= '')
                    resultado.append(nome)    
                    break
                        
    arquivo.close()
    return resultado         

cidades = carrega_cidades()


