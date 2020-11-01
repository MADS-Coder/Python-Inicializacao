from operator import itemgetter


def carregar(arquivo):
    linhas = []
    with open(arquivo) as f:
        f.readline()  # Descarta a primeira linha (cabeçalho do arquivo)
        for linha in f.readlines():
            data, abertura, alta, baixa, fechamento, volume = linha.strip().split(',')
            ano, mes, dia = data.split('-')
            linhas.append(
                {
                    "ano": int(ano),
                    "mes": int(mes),
                    "dia": int(dia),
                    "abertura": float(abertura),
                    "alta": float(alta),
                    "baixa": float(baixa),
                    "fechamento": float(fechamento),
                    "volume": int(volume),
                }
            )
    return linhas


def formatar_data(linha):
    meses = (
        'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
        'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
    )
    d, m, a, = linha['dia'], linha['mes'], linha['ano']
    return f'{d:0>2d} de {meses[m - 1]} de {a}'


# Realiza o volume médio do arquivo de acordo com o mês e o ano informado.
def media_fechamento(empresa, m, a):
    soma = cont = 0
    ordenado = sorted(empresa, key=itemgetter('ano', 'mes', 'dia'))
    for p in ordenado:
        if p['mes'] == m and p['ano'] == a:
            soma += p['volume']
            cont += 1
    media = soma/cont
    return media

def main():
    # Carregar os dados da empresa a partir do arquivo csv
    nome = input("Nome do arquivo (por exemplo: 'daily_ABEV3.SA.csv'): ").strip()
    mes = int(input("Mês que deseja saber a média: "))
    ano = int(input("Ano que deseja saber a média: "))
    dados = carregar(nome)
    mv = media_fechamento(dados, mes, ano)
    print(f'O volume médio em {mes}/{ano} foi {mv:.0f}')


if __name__ == '__main__':
    main()
