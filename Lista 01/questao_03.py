# Questão 3
# Maria trabalha para uma construtora no setor de vendas. Constantemente, ela tem que calcular a área dos 
# terrenos vendidos. Como Maria é sua amiga há muito tempo, você resolveu ajudá-la criando um programa que lê 
# o comprimento e a largura e imprime a área total do terreno em metros quadrados.
# Resposta:

comprimento = float(input('Digite quantos metros de comprimento possui o terreno: '))
largura = float(input('Agora digite quantos metros de largura possui o terreno: '))

area = comprimento * largura

print(f'A área do terreno é de {area.__round__(1)} m2')