import pygame 
import os # integração de imagens
import random  # biblioteca

# declarando todas as constantes do jogo

TELA_LARGURA = 500
TELA_ALTURA = 800

IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join('imagens', 'pipe.png')))
IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join('imagens','base.png')))
IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('imagens','bg.png')))
IMAGENS_PASSARO = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imagens','bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imagens','bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imagens','bird3.png')))
    ]

pygame.font.init() #inicializando fonte de texto
FONTE_PONTOS = pygame.font.SysFont('arial', 50)

# criando os objetos do jogo
class Passaro():
    
    IMGS = IMAGENS_PASSARO

    #animações de rotação
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5

    # função de criação do pássaro
    def __init__(self, x, y): # vamos definir todas os atributos no instante da criação do objeto , por isso definimos dentro do __init__
        self.y = x
        self.y = y
        self.angulo = 0 # o pássaro começa com ângulo 0
        self.velocidade = 0 # o pássaro começa com velocidade 0 (só se movimenta em y) 
        self.altura = self.y
        self.tempo = 0 # tempo de cada pulo (tempo p/ realizar cada parábola)
        self.contagem_imagem = 0 # imagem 1, 2 ou 3 do pássaro
        self.imagem = IMAGENS_PASSARO[0]

    # função de pular
    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y

    def mover(self):
        # calcular o deslocamento
        self.tempo += 1
        deslocamento = 1.5*(self.tempo**2) + self.tempo*self.velocidade # formula do sorvetão

        # restringir o deslocamento
        if deslocamento > 16:
            deslocamento == 16
        elif deslocamento < 0:
            deslocamento -= 2

        self.y += deslocamento
        
        # o angulo do passaro
        if deslocamento < 0 or self.y < (self.altura + 50):
            if self.angulo < self.ROTACAO_MAXIMA:
                self.angulo == self.ROTACAO_MAXIMA
        else:
            if self.angulo > -90:
                self.angulo -= self.VELOCIDADE_ROTACAO

    def desenhar(self):