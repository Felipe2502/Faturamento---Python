faturamento = input("Digite o faturamento desse mês:")
faturamento = faturamento.replace("R$", "")
faturamento = float(faturamento)

print(faturamento)

custo = 300

lucro = faturamento - custo
print(f"O faturamento foi de {faturamento} e o lucro foi de {lucro}")