# Questão 13
# Bem, nesse desafio, você deve informar se a data do dia faz parte da primavera ou do outono. Um dia está na 
# primavera se estiver entre 22/09 à 21/12 e o outono de datas entre 20/03 à 21/06.
# Resposta:

# Entrada da data
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))

# Verifica se a data está na primavera
if (mes == 9 and dia >= 22 and dia <= 30) or (mes == 10 and dia >= 1 and dia <= 31) \
   or (mes == 11 and dia >= 1 and dia <= 30) or (mes == 12 and dia >= 1 and dia <= 21):
    print(f"{dia:02d}/{mes:02d} está na primavera.")

# Verifica se a data está no outono
elif (mes == 3 and dia >= 20 and dia <= 31) or (mes == 4 and dia >= 1 and dia <= 30) \
     or (mes == 5 and dia >= 1 and dia <= 31) or (mes == 6 and dia >= 1 and dia <= 21):
    print(f"{dia:02d}/{mes:02d} está no outono.")

else:
    print(f"{dia:02d}/{mes:02d} não está na primavera nem no outono.")
