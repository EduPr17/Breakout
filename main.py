from Kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty

class BreakoutGame(Widget):
  pass

class BreakoutApp(App):
  def build(self):
    return BreakoutGame()

class BreakoutBall(Widget):
  
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    
    
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    
    def move(self):
      self.pos = Vector(*self.velocity) + self.pos

if __name__ == '__main__':
  BreakoutApp().run()
