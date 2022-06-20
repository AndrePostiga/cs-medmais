import locale

def formata_preco_em_centavos(preco: int) -> str:
    preco_em_decimal = preco / 100
    locale.setlocale(locale.LC_ALL, 'pt_BR')
    return locale.currency(preco_em_decimal, grouping=True)