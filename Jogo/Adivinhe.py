from random import randint
computador = randint(0,10)

print('-'*29)
print('JOGO ADIVINHE O NÚMERO')
print('_'*29)

acerta = False
palpite = 0

print('Em que número estou pensando?')

while not acerta:
    
    jogador = int(input('Escolha um número:'))
       
    palpite +=1
              
    if computador < jogador:
        print('Eu escolhi um número menor')
        
    elif computador > jogador:
        print('Eu escolhi um número maior')
        
    elif jogador == computador:
        acerta = True
        break
    

print(f'Você acertou com {palpite} tentativas')








