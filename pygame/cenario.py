import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Cenário em Movimento")

# Carrega a imagem de fundo
fundo = pygame.image.load("C:\Users\gabri\OneDrive\Documentos\COdes\UFMA_COdes\pygame\e4fba522-e852-4072-9fd1-e8497d533258.png").convert()
largura_fundo = fundo.get_width()

# Variáveis de movimento
x_fundo = 0
velocidade = 5

# Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move o fundo
    x_fundo -= velocidade
    if x_fundo <= -largura_fundo:
        x_fundo = 0

    # Desenha o fundo
    tela.blit(fundo, (x_fundo, 0))
    tela.blit(fundo, (x_fundo + largura_fundo, 0))

    # Atualiza a tela
    pygame.display.flip()
    pygame.time.Clock().tick(60)