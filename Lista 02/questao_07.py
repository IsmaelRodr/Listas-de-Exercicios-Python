# Questão 07
# Você agora quer fazer um programa apenas para exercitar a sua lógica. Basicamente, você viu que o IBGE faz uma 
# consulta de 5 preços para ver a média de preços. Você resolveu fazer o seguinte: ler os valores, calcular a 
# média e verificar quais valores estão acima da média. 
# Resposta:

precos = [4.50, 7.20, 8.75, 4.30, 6.85]

media = sum(precos) / len(precos)

for i in range(len(precos)):
    if precos[i] > media:
        print(f'O preço {i+1} ({precos[i]}): Está acima da média ({media})')

