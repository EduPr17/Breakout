import pygame
#SCREEN SIZE
SCREEN_SIZE = 650, 490
# DEFINING THE STRUCTURES 
BRICK_WIDTH = 62
BRICK_HEIGHT = 17
PADDLE_WIDTH = 62
PADDLE_HEIGHT = 12
BALL_DIAMETER = 16
BALL_RADIUS = BALL_DIAMETER / 2
# SETTING THE MAX DISTANCE THAT THE PADDLE AND THE BALL CAN GO ON THE SCREEN
MAX_PADDLE_X = SCREEN_SIZE[0] - PADDLE_WIDTH
MAX_BALL_X = SCREEN_SIZE[0] - BALL_DIAMETER
MAX_BALL_Y = SCREEN_SIZE[1] - BALL_DIAMETER
#PADDLE Y COORDINATE... NOT BEING ABLE TO MOVE UP AND JUST RIGHT TO LEFT
PADDLE_Y = SCREEN_SIZE - PADDLE_HEIGHT - 10
#DEFINING SOME COLORS
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (255, 0, 255)
BRICK_COLOR = (0, 0, 255)
# GAME STATES
STATE_BALL_IN_PADDLE = 0
STATE_PLAYING = 1
STATE_WON = 2
STATE_OVER = 3

class Breakout:
  def __init__():
    
    self.screen = pygame.display.set_mode(SCREEN_SIZE)
    
    if pygame.font:
      self.font = pygame.font.Font = (None, 30)
    else:
      self.font = None
      
    self.init_game()
    
  def init_game(self):
    self.lives = 3
    self.score = 0
    self.state = STATE_BALL_IN_PADDLE
    
    self.paddle = pygame.Rect(200, PADDLE_Y, PADDLE_HEIGHT, PADDLE WIDTH)
    self.ball = pygame.Rect(200, PADDLE_Y, BALL_DIAMETER, BALL_DIAMETER, BALL_DIAMETER)
    
    self.ball_vel = [5, -5]
    self.create_bricks()
    
  def create_bricks(self):
    

if __name__ == '__main__':
  Breakout().run()
