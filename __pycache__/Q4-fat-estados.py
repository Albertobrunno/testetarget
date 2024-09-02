# faturamento
faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}
total_faturamento = 0
for valor in faturamento.values():
    total_faturamento += valor
print("Percentual de representação por estado:")
for estado in faturamento:
    valor = faturamento[estado]
    percentual = (valor / total_faturamento) * 100
    print(estado + ": " + "{:.2f}".format(percentual) + "%")
