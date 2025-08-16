# Questão 2
# Você está começando na academia hoje e a sua instrutora fez um levantamento do seu biotipo, além de outras 
# informações suas. Ela para calcular o seu IMC (Índice de Massa Corporal), mediu o seu peso e sua altura. Com 
# essas informações em mãos, ela calculou o seu IMC usando a seguinte fórmula: imc = peso / (altura * altura). 
# Com o valor calculado, ela te apresentou a sua ficha de acompanhamento. Você resolveu ajudar a sua 
# instrutora e vai fazer um programa para calcular o imc. 
# Resposta:

peso = float(input('Digite seu peso (em kg): '))
altura = float(input('Digite sua altura (em metros): '))

imc = peso / (altura * altura)

print(f'Seu IMC é de {imc.__round__(1)} kg/m2')
