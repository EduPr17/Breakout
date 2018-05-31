import pygame
#SCREEN SIZE
screen_size = 640, 480
screen = pygame.display.set_mode(screen_size)

class Breakout(pygame.sprite.Sprite):
  def __init__(self, color, width, height):
    super().__init__()
    
    self.image = pygame.Surface([paddle_width, paddle_height)
    self.image.fill(paddle_color)
                                 
  def __init__(self, color, width, height):
    
    super().__init__()
    
                                 


brick_width = 64
brick_height = 48
paddle_width = 64
paddle_height = 48
ball_diameter = 20
ball_radius = ball_diameter / 2
ball_color = [255, 0, 255]
ball_x = 50
ball_y = 100

paddle_color = [0, 255, 0]


    
   
    
    self.init_game()
    
  def init_game(self):
    self.lives = 3
    self.score = 0

    
  def create_bricks(self):
    bricks_list = []
    for i in range(1,8):
      brick1 = Brick(75*i, 50)
      bricks_list.append(brick1)
    
