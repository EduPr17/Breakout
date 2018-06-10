import sys
import pygame

screen_size = 640,480

brick_width = 64
brick_height = 48
paddle_width = 64
paddle_height = 43
ball_diameter = 18
ball_radius = ball_diameter / 2

max_paddle_y = screen_size[0] - paddle_width
max_ball_x = screen_size[0] - ball_diameter
max_ball_y = screen_size[1] - ball_diameter

paddle_y = screen_size[1] - paddle_height - 10

black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
brick_color = (255,0,255)

state_ball_in_rest = 0
state_playing = 1
state_won = 2
state_game_over = 3

class Breakout:

  def __init__(self):
    pygame.init()
    
    self.screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Breakout Game")
    
    self.clock = pygame.time.Clock()
    
    if pygame.font:
      self.font = pygame.font.Font(None, 30)
    else:
      self.font = None
      
    self.init_game()
    
  def init_game(self):
    self.tries = 3
    self.score = 0
    self.state = state_ball_in_rest
    
    self.paddle = pygame.Rect(300, paddle_y, paddle_width, paddle_height)
    self.ball = pygame.Rect(300, paddle_y - ball_diameter, ball_diameter, ball_diameter)
    
    self.ball_vel = [5, -5]
    
    self.create_bricks()
    
  def create_bricks(self):
    y_ofs = 35
    self.bricks = []
    for i in range(7):
      x_ofs = 35
      for j in range(8):
        self.bricks.append(pygame.Rect(x_ofs,y_ofs,brick_width,brick_height))
        x_ofs += brick_width + 10
      y_ofs += brick_height + 5  
        
  def print_bricks(self):
    for brick in self.bricks:
      pygame.draw.rect(self.screen, brick_color, brick)
  
  def check_input(self):
    keys = pygame.keys.get_pressed()
    
    if keys[pygame.K_LEFT]:
      self.paddle.left -= 5
      if self.paddle.left < 0:
        self.paddle.left = 0
    
    if keys[pygame.K_RIGHT]:
      self.paddle.left += 5
      if self.paddle.left > max_paddle_x:
        self.paddle.left = max_paddle_x
        
    if keys[pygame.K_SPACE] and self.sate == state_ball_in_rest:
      self.ball_vel = [5,-5]
      self.state = state.playing
    elif keys[pygame.K_RETURN] and (self.state == state_game_over or self.state == state_won):
      self.init_game()
  
  def move_ball(self):
    self.ball.left += self.ball_vel[0]
    self.ball.top += self.ball_vel[1]
    
    if self.ball.left <= 0:
      self.ball.left = 0
      self.ball_vel[0] = -self.ball_vel[0]
    elif self.ball.left >= max_ball_x:
      self.ball.left = max_ball_x
      self.ball_vel[0] = -self.ball_vel[0]
      
    if self.ball.top < 0:
      self.ball.top = 0
      self.ball_vel[1] = -self.ball_vel[1]
    elif self.ball.top >= max_ball_y:
      self.ball.top = max_ball_y
      self.ball_vel[1] = -self.ball_vel[1]
      
  def collisions(self):
    for brick in self.bricks:
      if self.bricks.colliderect(brick):
        self.score += 3
        self.ball_vel[1] = -self.ball_vel[1]
        self.bricks.remove(brick)
        break
      
      if len(self.bricks) == 0:
        self.state = state_won
      
      if self.ball.colliderect(self.paddle):
        self.ball.top = paddle_y - ball_diameter
        self.ball_vel[1] = -self.ball_vel[1]
      elif self.ball.top > self.paddle.top:
        self.tries -= 1
        if self.lives > 0:
          self.state = state_ball_in_rest
        else: 
          self.state = state_game_over
          
  def stats(self):
    if self.font:
      font_surface = self.font.render("POINTS: " + str(self.score) + "TRIES LEFT: " + str(self.tries), False, white)
      self.screen.blit(font_surface, (205,5))
  
  def show_message(self,message):
    if self.font:
      size = self.font.size(message)
      font_surface = self.font.render(message,False, white)
      x = (screen_size[0] - size[0]) / 2
      y = (screen_size[1] - size[1]) / 2
      self.screen.blit(font_surface, (x,y))
  
  def run(self):
    while 1:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit
      
      self.clock.tick(50)
      self.screen.fill(black)
      self.check.input()
      
      if self.state == state_playing:
        self.move_ball()
        self.collisions()
      elif self.state == state_ball_in_rest:
        self.ball.left = self.paddle.left + self.paddle.width / 2
        self.ball.top = self.paddle.top - self.ball.height
        self.show_message("PRESS SPACE TO LAUNCH BALL")
      elif self.state == state_game_over:
        self.show_message("TRY AGAIN! PRESS ENTER")
      elif self.state == state_won:
        self.show_message("GREAT JOB! PRESS ENTER TO PLAY AGAIN")
        
      self.draw_bricks()
      
      pygame.draw.rect(self.screen, white, self.paddle)
      
      pygame.draw.circle(self.screen, green, (self.ball.left + ball_radius, self.ball.top + ball_radius), ball_radius)
      
      self.stats()
      
      pygame.display.flip()

if __name__ == "__main__":
  Breakout().run.()
      
        
