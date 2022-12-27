import pygame
import animation
import level

class Soldier(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('Game/HeroKnight/Idle/HeroKnight_Idle_0.png')
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect(center = (x, y))
    def draw(self,dir,movement):
        if movement == 1:
            screen.blit(ANIME.update(0.1,3,dir) ,player.rect)
        if movement == 2:
            screen.blit(ANIME.update(0.1,2,dir) ,player.rect)
        if movement == 3:
            screen.blit(ANIME.update(0.1,2,dir) ,player.rect)
        if movement == 4:
            screen.blit(ANIME.update(0.1,4,dir) ,player.rect)
        else:
            screen.blit(ANIME.update(0.1,1,dir) ,player.rect)
class parallax(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.scroll = 0
    self.ground_image = pygame.image.load("Game/Parallax/ground.png").convert_alpha()
    self.ground_width = self.ground_image.get_width()
    self.ground_height = self.ground_image.get_height()
    self.bg_images = []
    for i in range(1, 6):
      self.bg_image = pygame.image.load(f"Game/Parallax/plx-{i}.png").convert_alpha()
      self.bg_image = pygame.transform.scale(self.bg_image,(1280,720))
      self.bg_images.append(self.bg_image)
      self.bg_width = self.bg_images[0].get_width()
  def draw_bg(self):
    for x in range(5):
      speed = 1
      for i in self.bg_images:
        screen.blit(i, ((x * self.bg_width) - self.scroll * speed, 0))
        speed += 0.2

ANIME = animation.Animation()        
player = Soldier(600,300,4)
world = level.World()
bg_p = parallax()
dir = 'xl'
player.rect.x , player.rect.y = world.process_data(level.world_data)

pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption('TANUJ YO')
game_icon = pygame.image.load('Game/HeroKnight/game_icon.png').convert_alpha()
pygame.display.set_icon(game_icon)
clock = pygame.time.Clock()
run = True

while run:
    bg_p.draw_bg()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    world.draw()
    level.decoration_group.draw(screen)
    level.water_group.draw(screen)
    level.exit_group.draw(screen)

    keys=pygame.key.get_pressed()
    if keys[pygame.K_LSHIFT]:
        player.draw(dir,1)
    if keys[pygame.K_d]:
        if bg_p.scroll < 3000:
            bg_p.scroll += 5
        dir = 'xl'
        player.draw(dir,2)
    elif keys[pygame.K_a]:
        if bg_p.scroll > 0:
            bg_p.scroll -= 5
        dir = 'xr'
        player.draw(dir,3)
    elif keys[pygame.K_f]:
        player.draw(dir,4)
    if keys[pygame.K_d] or keys[pygame.K_a] or keys[pygame.K_f] or keys[pygame.K_LSHIFT]:
        pass
    else:
        player.draw(dir,5)
    pygame.display.update()
    clock.tick(100)