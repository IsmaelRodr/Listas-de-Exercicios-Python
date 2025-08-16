# Questão 10
# Uma loja de tintas deseja informar para os clientes o melhor custo-benefício na compra de suas tintas. Você 
# foi contratado para desenvolver um programa que deverá pedir o tamanho em metros quadrados da área a ser 
# pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é 
# vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. Informe 
# ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações: 
# a. comprar apenas latas de 18 litros;
# b. comprar apenas galões de 3,6 litros;
# c. misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre 
# arredonde os valores para cima, isto é, considere latas cheias.
# Resposta:

import math  # para arredondar para cima

# Entrada
area = float(input("Digite o tamanho da área a ser pintada (em m²): "))

# Acrescentar 10% de folga
area_com_folga = area * 1.10

# Cálculo de litros necessários (1 litro para cada 6 m²)
litros_necessarios = area_com_folga / 6

# Preços e capacidades
litros_lata = 18
preco_lata = 80.00
litros_galao = 3.6
preco_galao = 25.00

# a) Apenas latas
qtd_latas = math.ceil(litros_necessarios / litros_lata)
custo_latas = qtd_latas * preco_lata

# b) Apenas galões
qtd_galoes = math.ceil(litros_necessarios / litros_galao)
custo_galoes = qtd_galoes * preco_galao

# c) Mistura de latas e galões
qtd_latas_mistura = int(litros_necessarios // litros_lata)
resto_litros = litros_necessarios - (qtd_latas_mistura * litros_lata)
qtd_galoes_mistura = math.ceil(resto_litros / litros_galao)
custo_mistura = (qtd_latas_mistura * preco_lata) + (qtd_galoes_mistura * preco_galao)

# Saída
print("\n--- Resultado ---")
print(f"Apenas latas de 18L: {qtd_latas} lata(s) - Custo: R$ {custo_latas:.2f}")
print(f"Apenas galões de 3,6L: {qtd_galoes} galão(ões) - Custo: R$ {custo_galoes:.2f}")
print(f"Mix latas+galões: {qtd_latas_mistura} lata(s) e {qtd_galoes_mistura} galão(ões) - Custo: R$ {custo_mistura:.2f}")
