import json


with open("dados.json", "r") as f:
    dados = json.load(f)


valores = [dia["valor"] for dia in dados if dia["valor"] > 0]


menor = min(valores)
maior = max(valores)
media = sum(valores) / len(valores)

dias_acima_media = sum(1 for v in valores if v > media)


print(f"Menor faturamento do mês: R$ {menor:.2f}")
print(f"Maior faturamento do mês: R$ {maior:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
