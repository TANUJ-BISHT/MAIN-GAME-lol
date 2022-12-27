import pygame


def change_size(frame_list):
    mt = []
    for frames in frame_list:
        mt.append(pygame.transform.scale2x(frames))
    return mt

class Animation(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player_idle = [pygame.image.load('Game/HeroKnight/Idle/HeroKnight_Idle_0.png'),
                            pygame.image.load('Game/HeroKnight/Idle/HeroKnight_Idle_1.png'),
                            pygame.image.load('Game/HeroKnight/Idle/HeroKnight_Idle_2.png'),
                            pygame.image.load('Game/HeroKnight/Idle/HeroKnight_Idle_3.png'),
                            pygame.image.load('Game/HeroKnight/Idle/HeroKnight_Idle_4.png'),
                            pygame.image.load('Game/HeroKnight/Idle/HeroKnight_Idle_5.png'),
                            pygame.image.load('Game/HeroKnight/Idle/HeroKnight_Idle_6.png'),
                            pygame.image.load('Game/HeroKnight/Idle/HeroKnight_Idle_7.png')]

        self.player_run = [pygame.image.load('Game/HeroKnight/Run/HeroKnight_run_0.png'),
                           pygame.image.load('Game/HeroKnight/Run/HeroKnight_run_1.png'),
                           pygame.image.load('Game/HeroKnight/Run/HeroKnight_run_2.png'),
                           pygame.image.load('Game/HeroKnight/Run/HeroKnight_run_3.png'),
                           pygame.image.load('Game/HeroKnight/Run/HeroKnight_run_4.png'),
                           pygame.image.load('Game/HeroKnight/Run/HeroKnight_run_5.png'),
                           pygame.image.load('Game/HeroKnight/Run/HeroKnight_run_6.png'),
                           pygame.image.load('Game/HeroKnight/Run/HeroKnight_run_7.png'),
                           pygame.image.load('Game/HeroKnight/Run/HeroKnight_run_8.png'),
                           pygame.image.load('Game/HeroKnight/Run/HeroKnight_run_9.png')]

        self.player_jump = [pygame.image.load('Game/HeroKnight/Jump/HeroKnight_jump_0.png'),
                            pygame.image.load('Game/HeroKnight/Jump/HeroKnight_jump_1.png'),
                            pygame.image.load('Game/HeroKnight/Jump/HeroKnight_jump_2.png')]

        self.player_attack = [pygame.image.load('Game/HeroKnight/Attack1/HeroKnight_Attack1_0.png'),
                              pygame.image.load('Game/HeroKnight/Attack1/HeroKnight_Attack1_1.png'),
                              pygame.image.load('Game/HeroKnight/Attack1/HeroKnight_Attack1_2.png'),
                              pygame.image.load('Game/HeroKnight/Attack1/HeroKnight_Attack1_3.png'),
                              pygame.image.load('Game/HeroKnight/Attack1/HeroKnight_Attack1_4.png'),
                              pygame.image.load('Game/HeroKnight/Attack1/HeroKnight_Attack1_5.png')]

        self.player_jump = change_size(self.player_jump)
        self.player_run = change_size(self.player_run)
        self.player_idle = change_size(self.player_idle)
        self.player_attack = change_size(self.player_attack)
        self.current_frame = 0
    def update(self,speed,player_list,dir):
        if player_list == 1:
            player_list = self.player_idle
        if player_list == 2:
            player_list = self.player_run
        if player_list == 3:
            player_list = self.player_jump
        if player_list == 4:
            player_list = self.player_attack
        self.current_frame += speed
        if int(self.current_frame) >= len(player_list):
            self.current_frame = 0
        if dir == 'xl':
            return player_list[int(self.current_frame)]
        if dir == 'xr':
            return pygame.transform.flip(player_list[int(self.current_frame)],True,False)