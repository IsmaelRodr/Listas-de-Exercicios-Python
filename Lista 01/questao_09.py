# Questão 9
# A sua professora de Física passou uma questão sobre velocidade média. Ela explicou que a velocidade média de 
# um corpo, por exemplo, um carro, é calculada dividindo a distância percorrido (em metros) pela quantidade de 
# tempo (em segundos). Desse modo, a velocidade = distancia / tempo. Você que não é besta foi logo fazendo um 
# programa que calculasse a velocidade média, apenas lendo a distância percorrida e o tempo gastado para 
# percorrê-lo. 
# Resposta:

distancia_percorrida_metros = float(input("Digite o numero da distancia percorrida em metros: "))
tempo_segundos = int(input("Digite o numero do tempo em segundos: "))

velocidade = distancia_percorrida_metros / tempo_segundos

print(f'A velocidade é de {velocidade.__round__(1)} m/s')
