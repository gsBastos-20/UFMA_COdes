# Inicializa o Pygame

import pygame
pygame.init()

# Configurações da tela
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Texto Pixel Art no Pygame")

# Cor
BRANCO = (255, 255, 255)

# Carregar a fonte pixelada
fonte_pixel = pygame.font.Font("8-bit-hud.tff", 48)  # Defina o tamanho da fonte

# Renderizar o texto
texto = fonte_pixel.render("Hello, Pygame!", True, BRANCO)

# Loop principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Preencher a tela com preto
    tela.fill((0, 0, 0))

    # Desenhar o texto na tela
    tela.blit(texto, (200, 250))

    # Atualizar a tela
    pygame.display.flip()

# Fechar o Pygame
pygame.quit()