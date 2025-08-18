# Questão 10
# A minha sobrinha está aprendendo as letras do alfabeto. Ela ainda confunde o que é vogal e consoante. Você 
# topou fazer comigo um programa que verifica se uma letra é vogal ou consoante. Então, é isso, né? Vamos lá? 
# Respostas:

letra = 'd'

vogais = ['a','e','i','o','u']

is_consoante = letra != vogais[0] and letra != vogais[1] and letra != vogais[2] and letra != vogais[3] and letra != vogais[4]

if is_consoante:
    print(f'É consoante!')
else:
    print(f'É vogal!')