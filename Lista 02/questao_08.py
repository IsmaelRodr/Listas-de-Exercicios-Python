# Questão 08
# Em um jogo de tabuleiro, um jogador pode movimentar uma peça apenas se o número do seu dado for maior que o do 
# seu adversário. Faça um programa que informe se o jogador pode ou não jogar aquela partida. Leia o número do 
# dado do jogador e do seu adversário e informe quem deve jogar. No caso de empate, nenhum dos jogadores joga.
# Resposta:

dado_jogador = 3
dado_adversario = 5

is_jogador_joga = dado_jogador > dado_adversario
is_adversario_joga = dado_adversario > dado_jogador
is_empate = dado_jogador == dado_adversario

match True:
    case _ if is_jogador_joga:
        print('Jogador Joga')
    case _ if is_adversario_joga:
        print('Adversario Joga')
    case _ if is_empate:
        print('Deu empate, Ninguem joga, ambos devem jogar o dado novamente.')