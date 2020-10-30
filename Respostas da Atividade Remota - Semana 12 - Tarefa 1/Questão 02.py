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


def maior_volume(empresa):
    ordenado = sorted(empresa, key=itemgetter('volume'))
    return ordenado[-1]['volume'], formatar_data(ordenado[-1])


def menor_volume(empresa):
    ordenado = sorted(empresa, key=itemgetter('baixa'))
    return ordenado[0]['baixa'], formatar_data(ordenado[0])


def periodo_inicio(empresa):
    ordenado = sorted(empresa, key=itemgetter('ano', 'mes', 'dia'))
    return formatar_data(ordenado[0])


def periodo_final(empresa):
    ordenado = sorted(empresa, key=itemgetter('ano', 'mes', 'dia'), reverse=True)
    return formatar_data(ordenado[0])


def media_fechamento(empresa):
    return sum(valor['fechamento'] for valor in empresa) / len(empresa)


def main():
    n = input('Nome do arquivo com a extensão (exemplo: daily_ABEV3.SA.csv): ')

    # Carregar os dados da empresa a partir do arquivo csv
    nome = carregar(n)

    # Qual o maior volume diário negociado e em que data ocorreu.
    baixa, data = menor_volume(nome)
    print(f'O menor preço no fechamento foi {baixa:.2f} em {data}')


if __name__ == '__main__':
    main()
