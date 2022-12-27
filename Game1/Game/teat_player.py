import pygame
import animation
pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

#define game variables
ROWS = 16
COLS = 150
TILE_SIZE = SCREEN_HEIGHT // ROWS
TILE_TYPES = 21
score = 0
ANIME = animation.Animation()
class Soldier(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('Game/HeroKnight/Idle/HeroKnight_Idle_0.png')
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect(center = (x, y))
    def draw(self,dir,movement):
        if movement == 1:
            screen.blit(ANIME.update(0.1,3,dir) ,player.rect)
        if movement == 2 or movement == 3:
            screen.blit(ANIME.update(0.1,2,dir) ,player.rect)
        if movement == 4:
            screen.blit(ANIME.update(0.1,4,dir) ,player.rect)
        else:
            screen.blit(ANIME.update(0.1,1,dir) ,player.rect)
player = Soldier(600,300,4)
dir = 'xl'

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill('sky blue')

    keys=pygame.key.get_pressed()
    if keys[pygame.K_LSHIFT]:
        player.draw(dir,1)
    if keys[pygame.K_d]:
        dir = 'xl'
        player.draw(dir,2)
    elif keys[pygame.K_a]:
        dir = 'xr'
        player.draw(dir,3)
    elif keys[pygame.K_f]:
        player.draw(dir,4)
    if keys[pygame.K_d] or keys[pygame.K_a] or keys[pygame.K_f] or keys[pygame.K_LSHIFT]:
        pass
    else:
        player.draw(dir,5)
    pygame.display.update()
    clock.tick(75)