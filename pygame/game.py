import pygame
import sys


pygame.init()


largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo Simples com Pygame")


green = ((127,255,0))
black = ((0, 0, 0))


personagem_imagem = pygame.image.load("pygame\png-clipart-charli-xcx-charli-xcx-3.png")  #Endereço da imagem
personagem_largura = personagem_imagem.get_width(50)  # Largura da imagem
personagem_altura = personagem_imagem.get_height(50)  # Altura da imagem


rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and personagem_x > 0:
        personagem_x -= personagem_velocidade
    if teclas[pygame.K_RIGHT] and personagem_x < largura - personagem_largura:
        personagem_x += personagem_velocidade
    if teclas[pygame.K_UP] and personagem_y > 0:
        personagem_y -= personagem_velocidade
    if teclas[pygame.K_DOWN] and personagem_y < altura - personagem_altura:
        personagem_y += personagem_velocidade

    
    tela.fill(green)

    
    pygame.draw.rect(tela, black, (personagem_x, personagem_y, personagem_largura, personagem_altura))

    
    pygame.display.flip()

    
    pygame.time.Clock().tick(60)


pygame.quit()
sys.exit()