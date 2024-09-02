import json
caminho_arquivo_json = 'Q3-fat.json'
with open(caminho_arquivo_json, 'r') as file:
    faturamento = json.load(file)
faturamento_filtrado = [dia['valor'] for dia in faturamento if dia['valor'] > 0]
menor_valor = min(faturamento_filtrado)
maior_valor = max(faturamento_filtrado)
media_mensal = sum(faturamento_filtrado) / len(faturamento_filtrado)
dias_acima_da_media = sum(1 for valor in faturamento_filtrado if valor > media_mensal)

# resultados
print(f"Menor valor de faturamento: R${menor_valor:.2f}")
print(f"Maior valor de faturamento: R${maior_valor:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
