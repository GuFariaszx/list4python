vendas_brutas = [(101, "Monitor", 5, 1200.0), (102, "Mouse", 50, 80.0), 
(103, "Teclado", 8, 150.0), (104, "Case", 3, 50.0)]

quantidade = []

for i in vendas_brutas:
    if i[2] < 10:
        quantidade.append(i[1])

print(f"\nOs produtos que estão com estoque baixo são: {quantidade}")

calculo = (vendas_brutas[0][3] * vendas_brutas[0][2] + vendas_brutas[1][3] * vendas_brutas[1][2]
+ vendas_brutas[2][3] * vendas_brutas[2][2] + vendas_brutas[3][3] * vendas_brutas[3][2])

print(f"\nO valor total do inventário é de: R${calculo}")

reajuste = 0.15
vendas_reajuste = []

for n in vendas_brutas:
    novo_preco = n[3] * (1 + reajuste)
    nova_tupla = (n[1], novo_preco)
    vendas_reajuste.append(nova_tupla)

print(f"\nVendas com reajuste implementado: ")
print(vendas_reajuste)
