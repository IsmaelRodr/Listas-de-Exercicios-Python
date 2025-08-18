# Questão 04
# Na sua escola, você faz três avaliações no ano e a sua nota final é a média aritmética dessas três avaliações. 
# Para você ser aprovado sua média deve ser maior ou igual a 7.0 pontos, caso contrário você estará reprovado. 
# Faça um programa para ler suas notas e dizer se você está aprovado ou reprovado.
# Resposta:

nota_1 = float(input('Digite o valor da sua primeira nota: '))
nota_2 = float(input('Digite o valor da sua segunda nota: '))
nota_3 = float(input('Digite o valor da sua terceira nota: '))

media = (nota_1 + nota_2 + nota_3) / 3

is_aprovado = media >= 7

if is_aprovado:
    print('Aprovado')
else:
    print('Reprovado')