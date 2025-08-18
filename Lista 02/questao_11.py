# Questão 11
# Você sabia que um ano tem 365 dias, 5 horas, 48 minutos e 48 segundos, aproximadamente? O calendário que temos 
# hoje passou por várias transformações ao longo da história, saindo de calendários lunares para solares, 
# tentando manter sempre a precisão quanto ao equinócio de primavera (quando começa a primavera). Se não 
# considerássemos esse tempo excedente no ano, considerando apenas os 365 dias, em 372 anos, nós estaríamos 
# adiantados 3 mês em relação ao sol, ou seja, estaríamos em junho, mas o sol estaria ainda em março. Por isso, 
# de 4 em 4 anos, o mês de fevereiro tem 29 dias e o ano é chamado de bissexto. Então, a regra para um ano ser 
# bissexto é:

# - ele precisa ser divisível por 4 
# - e se divisível por 100 precisa ser divisível por 400 ao mesmo tempo. 
# Exemplos:
#	1600, 2000, 2020, 2024 (anos bissextos), 
#   1900, 1800, 1700 (não são bissextos, apesar de serem divisíveis por 4, eles também se dividem por 100, mas 
# não por 400).

# Faça um programa que diga se um ano é bissexto ou não.
# Resposta:

ano = 2025

is_bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

if is_bissexto:
    print(f'O ano de {ano} é bissexto!')
else:
    print(f'O ano de {ano} não é bissexto!')



