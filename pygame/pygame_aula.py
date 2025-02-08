# janela do jogo

import pygame

# importando todas as variaveis e constantes.
from pygame.locals import *

# funçao de sair o jogo
from sys import exit

#funçao para sortear valores

from random import randint




#inicializar todas as funçoes do Pygame.
pygame.init()

#Configuraçoes da tela
largura = 990
altura = 555
x = largura/2 # aqui é pra colcocar ,ais ou menos na tela
y = altura/2
# variaveis para o obejeto de colisao
# a posiçao vai muda entre esses numeros quando colidirem

x_roxo = randint(40, 950)
y_roxo = randint(50, 520)

pontos = 0

#gerando textos(tamanho) = fonte/tamanho/negrito/italico
fonte_pixel = pygame.font.Font("8bit16.ttf", 40)

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Lengends Of The Jungle")
relogio = pygame.time.Clock() #fps do jogo
# loop principal
     # o while é o principal e for serve para detectar eventos ocorreu
while True:
    relogio.tick(60) # fps
    tela.fill((0, 0, 0))

    # o que vai ver escrito
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte_pixel.render(mensagem, False, (255,255,255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
# movimento por teclas
        '''if event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 20
            if event.key == K_d:
                x = x  + 20
            if event.key == K_w:
                y = y - 20
            if event.key == K_s:
                y = y + 20'''
    
    if pygame.key.get_pressed()[K_a]:
        x = x - 20
    if pygame.key.get_pressed()[K_d]:
        x = x + 20
    if pygame.key.get_pressed()[K_w]:
        y = y - 20
    if pygame.key.get_pressed()[K_s]:
        y = y + 20    

# desenhando na tela 
    ret_vermelho = pygame.draw.rect(tela, (255, 0, 0), (x,y,40,50))
    ret_roxo = pygame.draw.rect(tela, (255, 0, 255), (x_roxo,y_roxo, 50,60) )
     #criando colisoes
    
    if ret_vermelho.colliderect(ret_roxo):
      x_roxo = randint(40, 950)
      y_roxo = randint(50, 520)
      pontos += 1

         # a variavel x, y para da movimento 
    '''if y >= altura:
       y = 0
    y = y + 1'''
   
                                                           # 1 parametro: a tela onde ele vai ser desenhado
    #pygame.draw.circle(tela, (0, 123, 200), (300,260),40)       #  2  ´´´´´´´ : a cor do meu obejeto
    #pygame.draw.line(tela, (255,255,0), (390,0), (390,600), 5)  # 3 é a posiçao do objeto e largura e altura
                                                         
    tela.blit(texto_formatado, (450,40))
                                                    
    pygame.display.update()

 


    
 