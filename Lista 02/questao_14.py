# Questão 14
# Chega de trabalhar com datas! Agora vamos trabalhar com números aleatórios. Você está fazendo um sistema de 
# rifas. Você deve ler o número máximo da rifa, por exemplo: 30, 50, 100, assim como o número da rifa apostado 
# pelo usuário. Você deve fazer o sorteio e verificar se o número que o usuário escolheu foi o sorteado. Procure 
# como gerar números aleatórios na internet. 
# Respostas:

import random  # Biblioteca para gerar números aleatórios

# Entrada do usuário
numero_maximo = int(input("Digite o número máximo da rifa: "))
numero_usuario = int(input("Digite o número que você escolheu: "))

# Gera um número aleatório entre 1 e o número máximo
numero_sorteado = random.randint(1, numero_maximo)

# Mostra o número sorteado
print(f"Número sorteado: {numero_sorteado}")

# Verifica se o usuário ganhou
if numero_usuario == numero_sorteado:
    print("Parabéns! Você ganhou a rifa!")
else:
    print("Que pena! Você não ganhou dessa vez.")
