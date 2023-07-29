#importando a biblioteca pygame
import random
import pygame 

#importar tudo do pygame
from pygame.locals import *

#variáveis
tamanho_janela = (500,500)
tamanho_pixel = (10)
mensagem = "GAME OVER"

#função de colisao para retornar se uma é igual a outra
def colisao(pos1,pos2):
    return pos1 == pos2

#função para checar se a cobrinha está dentro do limite da janela do jogo
def off_limits(pos):
    if 0 <= pos[0] < tamanho_janela[0] and 0 <= pos[1] < tamanho_janela[1]:
        return False
    else:
        return True
    
#função para gerar aleatorio a posição da fruta na tela
#divide pelo tamanho do pixel para nao ultrapassar o limite que a cobrinha pode andar 
def random_on_grid():
    x = random.randint(0, tamanho_janela[0])
    y = random.randint(0, tamanho_janela[1])
    return x // tamanho_pixel * tamanho_pixel, y // tamanho_pixel * tamanho_pixel


#criando a tela 
pygame.init()
screen = pygame.display.set_mode(tamanho_janela)

#definindo o nome do jogo
pygame.display.set_caption("Snake")

posicao_snake = [(250,50), (260,50), (270,50)] #posição da parte do corpo da cobrinha
superficie_snake = pygame.Surface((tamanho_pixel, tamanho_pixel))  #tamanho da superficie q vai mostrar
superficie_snake.fill((177,156,217)) #cor da cobra
direcao_snake = K_LEFT #tecla esquerda

superficie_fruta = pygame.Surface((tamanho_pixel, tamanho_pixel)) #tamanho da superficie da fruta
superficie_fruta.fill((250,128,114)) #cor da fruta
posicao_fruta = random_on_grid()

             
#função para reiniciar o jogo
def restart_game():
    global posicao_snake
    global posicao_fruta
    global direcao_snake
    posicao_snake = [(250, 50), (260, 50), (270, 50)]
    direcao_snake = K_LEFT
    posicao_fruta = random_on_grid()

#enquanto for verdadeiro para continuar executando 
while True:
    pygame.time.Clock().tick(15) #definindo frame para poder executar o jogo
    screen.fill((0,0,0)) #pintar a tela de preto, para limpar a posição anterior da cobrinha

    for event in pygame.event.get(): #listar os eventos q ta rodando no jogo no momento
        if event.type == QUIT: #Se a tecla clicada for para sair do jogo
            pygame.quit() #sair do jogo
            quit()

        elif event.type == KEYDOWN: #Quando tecla for pressionada pra baixo
            if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]: #Se a tecla pressionada esta entre essas
                direcao_snake = event.key #alterar a direção 

    #mostrar a fruta
    screen.blit(superficie_fruta, posicao_fruta)

    #Se a fruta colidir com a cobrinha, aumenta a cobrinha e aparece a fruta em outro lugar
    if colisao(posicao_fruta, posicao_snake[0]):
        posicao_snake.append((-10, -10))
        posicao_fruta = random_on_grid()
     

    #mostrar na tela a posicao da cobrinha
    for pos in posicao_snake:
         screen.blit(superficie_snake, pos) 

    #começando o tamanho da cobrinha -1, seria a ultima posição da cobrinha(calda à cabeça), mover a última peça com a anterior
    for i in range(len(posicao_snake)-1, 0, -1):
        if colisao(posicao_snake[0], posicao_snake[i]): #se estiver colidindo com alguma posição dela mesma, vai reiniciar o jogo
            restart_game()
            break
        posicao_snake[i] = posicao_snake[i - 1]

    #se estiver fora dos limites da posição da cabeça da cobrinha, vai reiniciar o jogo
    if off_limits(posicao_snake[0]):
        restart_game()

    #condições para movimentação da cobrinha

    #No pygame as coordenadas começa no canto superior esquerdo, seria o ponto 0, conforme vai para direita sobe no eixo X, 
    #conforme desce aumenta no eixo Y, se quiser ir pra cima, tem q subtrair o eixo Y, anda de pixel em pixel
    if direcao_snake == K_UP: 
        posicao_snake[0] = (posicao_snake[0][0], posicao_snake[0][1] - tamanho_pixel)
    elif direcao_snake == K_DOWN:
        posicao_snake[0] = (posicao_snake[0][0], posicao_snake[0][1] + tamanho_pixel)
    elif direcao_snake == K_LEFT:
        posicao_snake[0] = (posicao_snake[0][0] - tamanho_pixel, posicao_snake[0][1])
    elif direcao_snake == K_RIGHT:
        posicao_snake[0] = (posicao_snake[0][0] + tamanho_pixel, posicao_snake[0][1])

    #atualizar 
    pygame.display.update()


                            