# Questão 09
# Um baralho contém 52 cartas de 4 tipos (naipes) diferentes: paus, espadas, copas e ouro. Em cada naipe, que 
# consiste de 13 cartas, 3 dessas cartas contêm as figuras do rei, da dama e do valete, respectivamente. Faça um 
# programa que leia um número de 1 a 13 e informe qual carta o número representa por extenso. Lembrando que temos 
# algumas cartas especiais: 1 (Ás), 11 (Jalete), 12 (Rainha), 13 (Rei). 
# Resposta:

carta = 1

is_as = carta == 1
is_jalete = carta == 11
is_rainha = carta == 12
is_rei = carta == 13
is_outra_carta = carta != 1 and carta != 11 and carta != 12 and carta != 13 and carta < 13

match True:
    case _ if is_as:
        print('Carta de nº: 1 (Ás)')
    case _ if is_jalete:
        print('Carta de nº: 11 (Jalete)')
    case _ if is_rainha:
        print('Carta de nº: 12 (Rainha)')
    case _ if is_rei:
        print('Carta de nº: 13 (Rei)')
    case _ if is_outra_carta:
        print(f'Carta de nº: {carta}')

