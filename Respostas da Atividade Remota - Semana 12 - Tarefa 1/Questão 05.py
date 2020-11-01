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


def periodo_inicio(empresa):
    ordenado = sorted(empresa, key=itemgetter('ano', 'mes', 'dia'))
    return formatar_data(ordenado[0])


def periodo_final(empresa):
    ordenado = sorted(empresa, key=itemgetter('ano', 'mes', 'dia'), reverse=True)
    return formatar_data(ordenado[0])


# Realiza o preço médio do arquivo de acordo com o mês e o ano informado.
def media_fechamento(empresa):
    mes = int(input("Mês que deseja saber a média: "))
    ano = int(input("Ano que deseja saber a média: "))
    print(f'Dias de {mes}/{ano} que houve queda no preço da ação:')
    ordenado = sorted(empresa, key=itemgetter('ano', 'mes', 'dia'))
    for p in ordenado:
        if p['mes'] == mes:
            if p['ano'] == ano:
                if p['abertura'] > p['fechamento']:
                    d = p['dia']
                    v = round(p['abertura'] - p['fechamento'], 3)
                    print(f"('{p['dia']:02d}/{p['mes']:02d}/{p['ano']}', {p['abertura']}, {p['fechamento']}, {v})")


def main():
    # Carregar os dados da empresa a partir do arquivo csv
    nome = input("Nome do arquivo (por exemplo: 'daily_ABEV3.SA.csv'): ").strip()
    dado = carregar(nome)
    media_fechamento(dado)


if __name__ == '__main__':
    main()
