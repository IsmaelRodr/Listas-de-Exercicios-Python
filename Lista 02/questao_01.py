# Questão 01
# Sofia tem oitos anos e está aprendendo os números, os antecessores e os sucessores. Você resolveu fazer um 
# programa para ajudá-la a saber se um número é sucessor de outro. Você basicamente pede como entrada um número, 
# depois o suposto sucessor, por fim exibe se o suposto sucessor é o sucessor mesmo. É tipo assim: Sofia insere 
# os números: 23 e, depois, 24 e você vai exibir: “O número 24 é sucessor de 23”, mas se Sofia colocar 23 e, 
# depois, 26, você deve exibir: “O número 26 não é sucessor de 23”.
# Resposta:

numero = 24
suposto_sucessor = 26

is_sucessor = suposto_sucessor == numero + 1

if is_sucessor:
    print(f'O número {suposto_sucessor} é sucessor de {numero}')
else:
    print(f'O número {suposto_sucessor} não é sucessor de {numero}')