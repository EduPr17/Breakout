import pygame
pygame.init()
#SCREEN SIZE
screen_size = 640, 480
screen = pygame.display.set_mode(screen_size)

class Breakout(pygame.sprite.Sprite):
  def __init__(self, color, x, y):
    super().__init__()
    
     self.image = pygame.Surface([block_width, block_height])
     self.image.fill(purple)
     self.rect = image.get_rect()
     
     self.rect.x = x
     self.rect.y = y 


class Ball(pygame.sprite.Sprite):
  
  speed = 11.0
  
  x = 0.0
  y = 180.0
  
  direction = 200
  
  width = 10
  height = 10
  
  def __init__(self):
    super().__init__():
      
    self.image = pygame.Surface([self.width, self.height])
    
    self.image,fill(green)
    
    self.rect = self.image.get_rect()
    
    self.screenwidth = pygame.display.get_surface().get_width()
    self.screenheight = pygame.display.get_surface().get_height()

brick_width = 64
brick_height = 48
paddle_width = 64
paddle_height = 48
ball_diameter = 20
ball_radius = ball_diameter / 2
ball_color = [255, 0, 255]
ball_x = 50
ball_y = 100
purple = (255, 0, 255)
green = (0, 255, 0)
paddle_color = [0, 255, 0]


    
   
    
    self.init_game()
    
  def init_game(self):
    self.lives = 3
    self.score = 0

    

    
