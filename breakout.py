import pygame
#SCREEN SIZE
screen_size = 650, 490
# DEFINING THE STRUCTURES 
brick_width = 62
brick_height = 17
paddle_width = 62
paddle_height = 12
ball_diameter = 16
ball_radius = ball_diameter / 2
# SETTING THE MAX DISTANCE THAT THE PADDLE AND THE BALL CAN GO ON THE SCREEN
max_paddle_x = screen_size[0] - paddle_width
max_ball_x = screen_size[0] - ball_diameter
max_ball_y = screen_size[1] - ball_diameter
#PADDLE Y COORDINATE... NOT BEING ABLE TO MOVE UP AND JUST RIGHT TO LEFT
paddle_y = screen_size[1] - paddle_height - 10
#DEFINING SOME COLORS
black = (0, 0, 0)
green = (0, 255, 0)
purple = (255, 0, 255)
brick_color = (0, 0, 255)
# GAME STATES
state_ball_in_paddle = 0
state_playing = 1
state_won = 2
state_over = 3

class Breakout:
  def __init__():
    
    self.screen = pygame.display.set_mode(screen_size)
    
    if pygame.font:
      self.font = pygame.font.Font = (None, 30)
    else:
      self.font = None
      
    self.init_game()
    
  def init_game(self):
    self.lives = 3
    self.score = 0
    self.state = state_ball_in_paddle
    
    self.paddle = pygame.Rect(200, paddle_y, paddle_height, paddle_width)
    self.ball = pygame.Rect(200, paddle_y, ball_diameter, ball_diameter, ball_diameter)
    
    self.ball_vel = [5, -5]
    self.create_bricks()
    
  def create_bricks(self):
    

if __name__ == '__main__':
  Breakout().run()
