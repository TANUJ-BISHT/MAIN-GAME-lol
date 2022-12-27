import pygame



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
      self.bg_images.append(self.bg_image)
      self.bg_width = self.bg_images[0].get_width()
  def draw_bg(self,screen):
    for x in range(5):
      speed = 1
      for i in self.bg_images:
        screen.blit(i, ((x * self.bg_width) - self.scroll * speed, 0))
        speed += 0.2