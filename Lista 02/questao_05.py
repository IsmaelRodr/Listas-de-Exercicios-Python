# Questão 05
# The Asa’s Club é um clube da cidade e você está trabalhando na portaria dela. As regras para comprar ingressos 
# para o clube são claramente machistas, mas elas são aplicadas. As mulheres que chegarem até as 22h não pagam a 
# entrada, mas depois desse horário, elas pagam metade do valor do ingresso. Os homens que chegarem até as 22h 
# pagam 70% do ingresso, enquanto depois desse horário pagam o valor integral. Você que não perdeu tempo, fez um 
# programa para a portaria. Eu fico me perguntando porque tu se mete nessas coisas sem ganhar um centavo, mas 
# tudo bem.
# Resposta:

valor_ingresso = 25
horario = 23
is_mulher = False

ingresso_metade_valor = valor_ingresso - (valor_ingresso * 0.5)
ingresso_70_porcento_valor = valor_ingresso - (valor_ingresso * 0.3)

is_ate_22h = horario <= 22

if is_mulher:
    if is_ate_22h:
        print('Mulher não paga nada até 22hrs.\nValor ingresso: R$: 0,00')
    else:
        print(f'Mulher paga metade do valor do ingresso depois das 22hrs.\nValor ingresso: R$: {ingresso_metade_valor.__round__(2)}')
else:
    if is_ate_22h:
        print(f'Homem paga 70% do valor do ingresso até 22hrs.\nValor ingresso: R$: {ingresso_70_porcento_valor.__round__(2)}')
    else:
        print(f'Homem paga valor total do ingresso depois das 22hrs.\nValor ingresso: R$: {valor_ingresso}')