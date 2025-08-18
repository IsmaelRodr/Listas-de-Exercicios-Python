# Questão 03
# Você sabe que o “par ou ímpar” é o modo tradicional de escolher algo pela sorte. Normalmente, as duas pessoas 
# usam apenas uma mão e escolhem o número de dedos que desejam. Você soma o total de dedos e verifica se o número 
# é ímpar ou par. Um número é par se a sua divisão inteira por 2 resta zero, um número é ímpar no caso contrário. 
# Então, faça isso. Leia o número de dedos da mão de cada jogador e diga se o resultado deu ímpar ou par.
# Resposta:

dedos_jogador_1 = 8
dedos_jogador_2 = 4

total_dedos = dedos_jogador_1 + dedos_jogador_2

is_par = total_dedos % 2 == 0

if is_par:
    print('O resultado deu par')
else:
    print('O resultado deu ímpar')