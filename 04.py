faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

faturamentoTotal = sum(faturamento.values())
percentualFaturamento = {}

for estado, valor in faturamento.items():
    percentual = (valor / faturamentoTotal) * 100
    percentualFaturamento[estado] = percentual

for estado, percentual in percentualFaturamento.items():
    print(f"{estado}: {percentual:.2f}%")