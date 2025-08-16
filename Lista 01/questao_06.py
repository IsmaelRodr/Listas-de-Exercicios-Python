# Questão 6
# O Bar do Boca é um bar conhecido na sua cidade. Todas as sextas-feiras, o bar tem música ao vivo e um novo 
# cardápio a cada mês. O dono do bar, Boca, não sabe mais o que fazer com as contas que são fechadas erradas, 
# pois os garçons esquecem de adicionar a taxa de couvert ou esquecem que a gorjeta sai de 10% para 20%. Você 
# que conhece o Boca há muito tempo resolveu ajudá-lo.  Você vai fazer um programa que ler o total da conta e 
# acrescenta 20% da gorjeta e a taxa fixa do couvert.
# Resposta:

total_conta = float(input("Digite o valor total da conta: R$ "))
taxa_couvert = float(input("Digite o valor da taxa de couvert: R$ "))

gorjeta = total_conta * 0.20

valor_final = total_conta + gorjeta + taxa_couvert

print("\nResumo da conta:")
print(f"Valor da conta: R$ {total_conta:.2f}")
print(f"Gorjeta (20%): R$ {gorjeta:.2f}")
print(f"Couvert: R$ {taxa_couvert:.2f}")
print(f"Total a pagar: R$ {valor_final:.2f}")
