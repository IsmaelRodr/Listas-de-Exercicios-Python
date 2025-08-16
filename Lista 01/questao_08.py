# Questão 8
# O IBGE (Instituto Brasileiro de Geografia e Estatística) para definir um preço médio de um produto 
# alimentar, por exemplo: o feijão, faz consulta a pelo menos 5 mercados de tamanhos variados. Após ler os 
# valores dos 5 mercados, o instituto calcula o valor médio do produto. Diferente do que era praticado antes, 
# atualmente, o IBGE utiliza um pequeno sistema para computar o preço médio. Você está trabalhando na equipe 
# de TI do IBGE para calcular o preço médio dos produtos. Lembre-se de ler os cinco preços, calcular a média e 
# exibir o resultado. 
# Resposta:

preco_1 = 7.49
preco_2 = 8.29
preco_3 = 6.99
preco_4 = 7.89
preco_5 = 6.59

media = (preco_1 + preco_2 + preco_3 + preco_4 + preco_5) / 5

print(f'A Média do valor dos produtos é de: R${media.__round__(2)}')