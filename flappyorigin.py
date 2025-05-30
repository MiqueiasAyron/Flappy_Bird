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
        self.x = x
        self.y = y
        self.angulo = 0 # o pássaro começa com ângulo 0
        self.velocidade = 0 # o pássaro começa com velocidade 0 (só se movimenta em y) 
        self.altura = self.y
        self.tempo = 0 # tempo de cada pulo (tempo p/ realizar cada parábola)
        self.contagem_imagem = 0 # imagem 1, 2 ou 3 do pássaro
        self.imagem = self.IMGS[0]

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
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 0 

        self.y += deslocamento
                  
        # o angulo do passaro
        if deslocamento < 0 or self.y < (self.altura + 50):
            if self.angulo < self.ROTACAO_MAXIMA:   
                self.angulo = self.ROTACAO_MAXIMA
        else:
            if self.angulo > -90:
                self.angulo -= self.VELOCIDADE_ROTACAO

    def desenhar(self,tela):
        # definir qual imagem do pássaro vai usar ( criar movimento de bater asas )
        self.contagem_imagem += 1
        if self.contagem_imagem < self.TEMPO_ANIMACAO:
            self.imagem = self.IMGS[0]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*2:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*3:
            self.imagem = self.IMGS[2]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*4:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*5:
            self.imagem = self.IMGS[0]
            self.contagem_imagem = 0

        # se o pássaro tiver caindo, não vai bater asas
        if self.angulo < -80:
            self.imagem = self.IMGS[1]
            self.contagem_imagem = self.TEMPO_ANIMACAO*2

        # desenhar a imagem
        imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo)
        pos_centro_imagem = self.imagem.get_rect(topleft=(self.x , self.y)).center
        rentangulo = imagem_rotacionada.get_rect(center = pos_centro_imagem)
        tela.blit(imagem_rotacionada, rentangulo.topleft)


# A imagem do pássaro é criada dentro de um retângulo. Portanto, nas condições de 
# colisão, o programa iria detectar colição com o retângulo que circunda a imagem do
# pássaro gerando uma espécie de bug no jogo e comprometendo a jogabilidade. Para e-
# vitar isso, vamos criar uma MASK; vamos dividir o retângulo em vários pixels. Assim,
# a colisão vai ser verificada averiguando se dentro de um mesmo pixel existe cano e 
# pássaro.

    def get_mask(self):
        return pygame.mask.from_surface(self.imagem)

class Cano():
    DISTANCIA = 200 # distância entre os canos de cima e de baixo
    VELOCIDADE = 5 # velocidade horizontal do cano

    def __init__(self, x):
        self.x = x
        self.altura = 0
        self.pos_topo = 0
        self.pos_base = 0
        self.CANO_TOPO = pygame.transform.flip(IMAGEM_CANO, False, True)
        self.CANO_BASE = IMAGEM_CANO
        self.passou = False
        self.definir_altura()

    def definir_altura(self):
        self.altura = random.randint(50,450)
        self.pos_topo = self.altura - self.CANO_TOPO.get_height()
        self.pos_base  = self.altura + self.DISTANCIA

    def mover(self):
        self.x -= self.VELOCIDADE
    
    def desenhar(self, tela):
        tela.blit(self.CANO_TOPO, (self.x, self.pos_topo))
        tela.blit(self.CANO_BASE, (self.x, self.pos_base))

    def colidir(self, passaro):
        passaro_mask = passaro.get_mask()
        topo_mask = pygame.mask.from_surface(self.CANO_TOPO)
        base_mask = pygame.mask.from_surface(self.CANO_BASE)
 
        distancia_topo = (self.x - passaro.x , self.pos_topo - round(passaro.y))
        distancia_base = (self.x - passaro.x , self.pos_base - round(passaro.y))

        topo_ponto = passaro_mask.overlap(topo_mask, distancia_topo)   
        base_ponto = passaro_mask.overlap(base_mask, distancia_base)

        if base_ponto or topo_ponto:
            return True
        else:
            return False
        
class Chao():
    VELOCIDADE = 5
    LARGURA = IMAGEM_CHAO.get_width()
    IMAGEM =  IMAGEM_CHAO

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.x1 + self.LARGURA

    def mover(self):
        self.x1 -= self.VELOCIDADE
        self.x2 -= self.VELOCIDADE

        if self.x1 + self.LARGURA < 0:
            self.x1 = self.x2 + self.LARGURA
        if self.x2 + self.LARGURA < 0: 
            self.x2 = self.x1 + self.LARGURA

    def desenhar(self, tela):
        tela.blit(self.IMAGEM,(self.x1, self.y))
        tela.blit(self.IMAGEM, (self.x2, self.y))
    
def desenhar_tela(tela, passaros, canos, chao, pontos):
    tela.blit(IMAGEM_BACKGROUND, (0,0))
    for passaro in passaros:
        passaro.desenhar(tela)
    for cano in canos:
        cano.desenhar(tela)
    texto = FONTE_PONTOS.render(f'score: {pontos}', 1, (255,255,255))
    tela.blit(texto, (TELA_LARGURA - 10 - texto.get_width() , 10))
    chao.desenhar(tela)
    pygame.display.update()    

def main():
    passaros = [Passaro(230,350)]
    chao = Chao(730)
    canos = [Cano(700)]
    tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
    pontos = 0
    relogio = pygame.time.Clock()

    rodando = True
    while rodando :
        relogio.tick(30) # 30 fps ( 30 frames por segundos)

        # interação com o usuário
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    for passaro in passaros:
                        passaro.pular()
        
        # mover as coisas 
        for passaro in passaros:
            passaro.mover() 
        chao.mover()

        adicionar_cano = False
        remover_canos = []
        for cano in canos:
            for i, passaro in enumerate(passaros):
                if cano.colidir(passaro):
                    passaro.pop(i) # o pássaro que colide será removido
                if not cano.passou and passaro.x > cano.x:
                    cano.passou = True
                    adicionar_cano = True
                cano.mover()
                if cano.x + cano.CANO_TOPO.get_width() < 0:
                    remover_canos.append(cano)
        
        if adicionar_cano:
            pontos += 1
            canos.append(Cano(600))
        for cano in remover_canos:
            canos.remove(cano)

        for i, passaro in enumerate(passaros):
            if (passaro.y + passaro.imagem.get_height()) > 730 or passaro.y < 0:
                passaros.pop(i)

        desenhar_tela(tela, passaros, canos, chao, pontos)

if __name__ == '__main__':
    main()