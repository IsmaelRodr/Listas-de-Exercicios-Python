# Questão 9
# A sua professora de Física passou uma questão sobre velocidade média. Ela explicou que a velocidade média de 
# um corpo, por exemplo, um carro, é calculada dividindo a distância percorrido (em metros) pela quantidade de 
# tempo (em segundos). Desse modo, a velocidade = distancia / tempo. Você que não é besta foi logo fazendo um 
# programa que calculasse a velocidade média, apenas lendo a distância percorrida e o tempo gastado para 
# percorrê-lo. 
# Resposta:

distancia_percorrida_metros = 500
tempo_segundos = 60

velocidade = distancia_percorrida_metros / tempo_segundos

print(f'A velocidade é de {velocidade.__round__(1)} m/s')
