# Questão 15
# As cores no computador podem ser representadas por número inteiros entre 0 e 255, ou seja, 256 valores 
# distintos, onde 0 (zero) representa preto e 255 representa branco. Nessa escala de cinza, os valores abaixo de 
# 128 são os mais escuros, acima desse valor os mais claros. Faça um programa que leia o nível de cinza, 
# verifique se o valor está entre 0 e 255 e depois diga se é tom escuro ou claro. 
# Resposta:

# Entrada do nível de cinza
nivel = int(input("Digite o nível de cinza (0 a 255): "))

# Verifica se o valor está dentro do intervalo válido
if nivel < 0 or nivel > 255:
    print("Valor inválido! O nível de cinza deve estar entre 0 e 255.")
else:
    # Verifica se é tom escuro ou claro
    if nivel < 128:
        print(f"Nível {nivel} é um tom escuro.")
    else:
        print(f"Nível {nivel} é um tom claro.")
