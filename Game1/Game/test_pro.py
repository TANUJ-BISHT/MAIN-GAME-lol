
import pygame
pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
FPS = 60

GRAVITY = 0.75
SCROLL_THRESH = 200
ROWS = 16
COLS = 150
TILE_SIZE = SCREEN_HEIGHT // ROWS
TILE_TYPES = 21
screen_scroll = 0
bg_scroll = 0
level = 1
start_game = False
start_intro = False

#define player action variables
moving_left = False
moving_right = False

class Soldier(pygame.sprite.Sprite):
	def __init__(self, x, y, scale, speed, ammo, grenades):
		pygame.sprite.Sprite.__init__(self)
		self.alive = True
		self.char_type = char_type
		self.speed = speed
		self.ammo = ammo
		self.start_ammo = ammo
		self.shoot_cooldown = 0
		self.grenades = grenades
		self.health = 100
		self.max_health = self.health
		self.direction = 1
		self.vel_y = 0
		self.jump = False
		self.in_air = True
		self.flip = False
		self.animation_list = []
		self.frame_index = 0
		self.action = 0
		self.update_time = pygame.time.get_ticks()
		#ai specific variables
		self.move_counter = 0
		self.vision = pygame.Rect(0, 0, 150, 20)
		self.idling = False
		self.idling_counter = 0
		
		#load all images for the players
		animation_types = ['Idle', 'Run', 'Jump', 'Death']
		for animation in animation_types:
			#reset temporary list of images
			temp_list = []
			#count number of files in the folder
			num_of_frames = len(os.listdir(f'img/{self.char_type}/{animation}'))
			for i in range(num_of_frames):
				img = pygame.image.load(f'img/{self.char_type}/{animation}/{i}.png').convert_alpha()
				img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
				temp_list.append(img)
			self.animation_list.append(temp_list)

		self.image = self.animation_list[self.action][self.frame_index]
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.width = self.image.get_width()
		self.height = self.image.get_height()

	def move(self, moving_left, moving_right):
		#reset movement variables
		screen_scroll = 0
		dx = 0
		dy = 0

		#assign movement variables if moving left or right
		if moving_left:
			dx = -self.speed
			self.flip = True
			self.direction = -1
		if moving_right:
			dx = self.speed
			self.flip = False
			self.direction = 1
		if self.jump == True and self.in_air == False:
			self.vel_y = -11
			self.jump = False
			self.in_air = True

		#apply gravity
		self.vel_y += GRAVITY
		if self.vel_y > 10:
			self.vel_y
		dy += self.vel_y

		#check for collision
		for tile in world.obstacle_list:
			#check collision in the x direction
			if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
				dx = 0
				#if the ai has hit a wall then make it turn around
				if self.char_type == 'enemy':
					self.direction *= -1
					self.move_counter = 0
			#check for collision in the y direction
			if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
				#check if below the ground, i.e. jumping
				if self.vel_y < 0:
					self.vel_y = 0
					dy = tile[1].bottom - self.rect.top
				#check if above the ground, i.e. falling
				elif self.vel_y >= 0:
					self.vel_y = 0
					self.in_air = False
					dy = tile[1].top - self.rect.bottom


		#check for collision with water
		if pygame.sprite.spritecollide(self, water_group, False):
			self.health = 0

		#check for collision with exit
		level_complete = False
		if pygame.sprite.spritecollide(self, exit_group, False):
			level_complete = True

		#check if fallen off the map
		if self.rect.bottom > SCREEN_HEIGHT:
			self.health = 0


		#check if going off the edges of the screen
		if self.char_type == 'player':
			if self.rect.left + dx < 0 or self.rect.right + dx > SCREEN_WIDTH:
				dx = 0

		#update rectangle position
		self.rect.x += dx
		self.rect.y += dy

		#update scroll based on player position
		if self.char_type == 'player':
			if (self.rect.right > SCREEN_WIDTH - SCROLL_THRESH and bg_scroll < (world.level_length * TILE_SIZE) - SCREEN_WIDTH)\
				or (self.rect.left < SCROLL_THRESH and bg_scroll > abs(dx)):
				self.rect.x -= dx
				screen_scroll = -dx

		return screen_scroll, level_complete





		    keys=pygame.key.get_pressed()
    if keys[pygame.K_LSHIFT] and jump is False:
        jump = True
    if jump is True:
        player_rect.y -= vel_y * 3
        if dir == 'xl':
            player_rect.x += 4
        else:
            player_rect.x -= 4 
        vel_y -= 0.5
        if vel_y < -10:
            jump = False
            vel_y = 10
        screen.blit(ANIME.update(0.15,3,dir),player_rect)