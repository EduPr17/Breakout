from Kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty

class BreakoutGame(Widget):
  pass

class BreakoutApp(App):
  def build(self):
    return BreakoutGame()


if __name__ == '__main__':
  BreakoutApp().run()
