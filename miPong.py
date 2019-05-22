import pygame,sys
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

# Colores RGB

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Pantalla
ANCHO_PANTALLA = 900
ALTO_PANTALLA = 600
FPS = 90

PANTALLA = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))

# pygame.display.set_caption('miPong')





class Jugador(pygame.sprite.Sprite):
    # Clase para la barra

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        alto_jugador = 85
        ancho_jugador = 14


        self.image = pygame.Surface((ancho_jugador, alto_jugador))
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.centerx
        self.rect.centery



class Bola(pygame.sprite.Sprite):
    # Clase para la pelota

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        diametro_bola = 14

        self.image = pygame.Surface((diametro_bola, diametro_bola))
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.centerx
        self.rect.centery
        self.velocidad = 2

    def mover(self):

        self.rect.centerx += self.velocidad
        self.rect.centery -= self.velocidad



# Creación de jugadores, pelota, y posición inicial
jugador1 = Jugador()
jugador1.rect.centerx = (ANCHO_PANTALLA -12)
jugador1.rect.centery = (ALTO_PANTALLA/2)

jugador2 = Jugador()
jugador2.rect.centerx = (12)
jugador2.rect.centery = (ALTO_PANTALLA/2)

pelota = Bola()
pelota.rect.centerx = (ANCHO_PANTALLA/2)
pelota.rect.centery = (ALTO_PANTALLA/2)

# Dibujar cuerpos
todos_sprites = pygame.sprite.Group()
todos_sprites.add(jugador1, jugador2)
pelota_sprite = pygame.sprite.Group()
pelota_sprite.add(pelota)


# Loop principal
x = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    x += 1
    print(x)



    PANTALLA.fill(NEGRO)

    pelota.mover()

    pelota_sprite.draw(PANTALLA)
    todos_sprites.draw(PANTALLA)
    pygame.display.set_caption("fps: " + str(clock.get_fps()))
    clock.tick(FPS)
    pygame.display.flip() # update





