# Questão 06
# Dessa vez, lhe iludiram e disseram que iam pagar para você fazer um programa, mas no fundo você sabe que não 
# vai receber. Você foi contratado para criar um programa de promoção do dia do consumidor. Basicamente, você vai 
# ler o total da compra de um consumidor e aplicar o desconto conforme abaixo:

#	total compra	desconto
#	< 50,00		    5%
#	< 100,00		10%
#   < 200,00		20%
#    < 500,00		25%
#    >= 500, 00		30%

# Por fim, você deve imprimir o valor total da compra após o desconto. 
#Resposta:

total_compra = 50

is_5_porcento_desconto = total_compra < 50
is_10_porcento_desconto = total_compra >= 50 and total_compra < 100
is_20_porcento_desconto = total_compra >= 100 and total_compra < 200
is_25_porcento_desconto = total_compra >= 200 and total_compra < 500
is_30_porcento_desconto = total_compra >= 500

valor_compra_desconto_5 = total_compra - (total_compra * 0.05)
valor_compra_desconto_10 = total_compra - (total_compra * 0.1)
valor_compra_desconto_20 = total_compra - (total_compra * 0.2)
valor_compra_desconto_25 = total_compra - (total_compra * 0.25)
valor_compra_desconto_30 = total_compra - (total_compra * 0.3)

match True:
    case _ if is_5_porcento_desconto:
        print(f'Total da compra (5% de desconto aplicado): R$: {valor_compra_desconto_5.__round__(2)}')
    case _ if is_10_porcento_desconto:
        print(f'Total da compra (10% de desconto aplicado): R$: {valor_compra_desconto_10.__round__(2)}')
    case _ if is_20_porcento_desconto:
        print(f'Total da compra (20% de desconto aplicado): R$: {valor_compra_desconto_20.__round__(2)}')
    case _ if is_25_porcento_desconto:
        print(f'Total da compra (25% de desconto aplicado): R$: {valor_compra_desconto_25.__round__(2)}')
    case _ if is_30_porcento_desconto:
        print(f'Total da compra (30% de desconto aplicado): R$: {valor_compra_desconto_30.__round__(2)}')