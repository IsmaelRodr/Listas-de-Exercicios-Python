# Questão 1
# Você trabalha em um supermercado e no caixa que você trabalha o consumidor só pode comprar um único
# produto, mesmo que várias unidades repetidas. Você deseja otimizar o seu trabalho e criar um programa que
# leia o preço do produto e a quantidade de itens comprados e informe o total da compra para o usuário. 
# Resposta:

preco = float(input('Insira o valor do produto: R$ '))
quant = float(input('Insira a quantidade de itens: '))
total = preco * quant
print(f'O valor total da sua compra é: R${total}')
