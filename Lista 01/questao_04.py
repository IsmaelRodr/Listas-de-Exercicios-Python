# Questão 4
# Maria amou o programa que você fez para ela de calcular a área dos terrenos, mas ela possui outro grande 
# problema: alguns terrenos não possuem lados uniformes, assim, ela precisa, muitas vezes, informar, além da 
# área, o perímetro do terreno. Ela confirmou a você que todos os terrenos só possuem quatro lados. Você sabe 
# que para calcular o perímetro do terreno basta somar todos os lados. Dessa forma, você confirmou a ela que 
# faria esse programa de calcular perímetro. 
# Resposta:

lado_1 = float(input('Informe o tamanho do primeiro lado do terreno (em metros): '))
lado_2 = float(input('Informe o tamanho do segundo lado do terreno (em metros): '))
lado_3 = float(input('Informe o tamanho do terceiro lado do terreno (em metros): '))
lado_4 = float(input('Informe o tamanho do quarto lado do terreno (em metros): '))

perimetro = lado_1 + lado_2 + lado_3 + lado_4

print(f'O perimetro do terreno é de {perimetro} metros')