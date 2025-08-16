# Questão 7
# Você saiu com seus amigos para ir ao cinema. Depois de assistirem o filme, vocês foram para um restaurante 
# comemorar o aniversário de sua amiga, Alice. Na hora de pagar a conta, como sempre, foi aquele furdunço, 
# divide daqui, divide dali. Então, você pensou: vou fazer um programa para calcular a conta por pessoa em um 
# aniversário. Claro que a aniversariante não conta. Deste modo, você faria um programa que lesse o total da 
# conta, divide-a pelo número de pessoas na mesa, menos o aniversariante. Depois, você só precisa exibir 
# quanto cada um tem que pagar. 
# Resposta:

total_conta = 50
qnt_pessoas = 6

dinheiro_por_pessoa = total_conta / (qnt_pessoas - 1)

print(f'O valor da conta a ser paga por pessoa, exeto a anivesariante é de: R${dinheiro_por_pessoa.__round__(2)}')