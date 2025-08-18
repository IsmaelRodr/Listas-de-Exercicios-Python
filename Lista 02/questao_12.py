# Questão 12
# Parabéns! Esse é o seu primeiro dia no estágio na rede de hotéis: DOM. O seu supervisor de estágio passou uma 
# demanda que eles estão tendo em produção. As datas não estão sendo validadas corretamente pela função da API, 
# então, ele resolveu pedir a você que desenvolvesse um programa que validasse a data. Você deve ler o dia, o mês 
# e o ano e ao fim imprimir se a data é válida ou não. Não esqueça de verificar se o ano é bissexto ou não (se 
# for bissexto, o mês de fevereiro terá 29 dias). 
# Resposta:


# Programa para validar datas

# Entrada da data
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

# Verifica se o ano é bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    bissexto = True
else:
    bissexto = False

# Dicionário com o número de dias de cada mês
dias_mes = {
    1: 31,
    2: 29 if bissexto else 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

# Validação da data
if mes not in dias_mes:
    print("Data inválida! Mês inexistente.")
elif dia < 1 or dia > dias_mes[mes]:
    print("Data inválida! Dia fora do intervalo do mês.")
else:
    print(f"{dia:02d}/{mes:02d}/{ano} é uma data válida!")
