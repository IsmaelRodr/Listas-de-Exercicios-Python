# Questão 5
# Você quer viajar para fora do Brasil, mas ainda não escolheu o seu destino. Você está em dúvida entre 
# Europa, Canadá, Estados Unidos e Argentina. Você sabe que as moedas nessas regiões são: euro, dólar 
# canadense, dólar americano, peso argentino. Você queria um programa que você desse o valor que deseja levar 
# e as cotações do dia de cada moeda e imprimisse quanto em cada moeda você teria. Então, resolveu que faria 
# esse programa para você e sua mãe verem quanto de dinheiro teriam em cada região. 
# Resposta:

valor_reais = 50

um_euro = 6.31 #reais
um_dolar_americano = 5.42 #reais
um_dolar_canadense = 3.92 #reais
um_peso_argentino = 0.0042 #reais

conversao_real_euro = valor_reais / um_euro
conversao_real_dolar_americano = valor_reais / um_dolar_americano
conversao_real_dolar_canadense = valor_reais / um_dolar_canadense
conversao_real_peso_argentino = valor_reais / um_peso_argentino

tabela = f"""
=======================
Na Europa terão: {conversao_real_euro.__round__(2)} euros,
Nos Estados unidos terão: {conversao_real_dolar_americano.__round__(2)} dolares americanos,
No Canadá terão: {conversao_real_dolar_canadense.__round__(2)} dolares canadenses,
Na Argentina terão: {conversao_real_peso_argentino.__round__(2)} pesos argentinos
=======================
"""

print(f'De acordo com a conversão do dinheiro: {tabela}')