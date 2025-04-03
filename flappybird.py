import pygame 
import os # integração de imagens
import random  # biblioteca

# declarando todas as constantes do jogo

TELA_LARGURA = 500
TELA_ALTURA = 800

IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join('imagens', 'pipe.png')))
IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join('imagens','base.png')))
IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('imagens','bg.png')))
IMAGENS_PÁSSARO = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imagens','bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imagens','bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imagens','bird3.png')))
    ]

pygame.font.init() #inicializando fonte de texto
FONTE_PONTOS = pygame.font.SysFont('arial', 50)

# criando os objetos do jogo
