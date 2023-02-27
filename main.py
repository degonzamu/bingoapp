from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window

import random


from kivy.uix.widget import Widget

class MyLabel(Label):
      pass

class BingoGame(BoxLayout):
   def __init__(self,**kwargs):
       super(BingoGame, self).__init__(**kwargs)
       self.values =list(range(1, 91))

   def calculate_random_number(self):
        random_value = random.choice(self.values)
        self.ids['label_value'].text = str(random_value)
        self.values.remove(random_value)
        layout = self.ids['values']
        lab1 = MyLabel(text=str(random_value), size_hint_x=1, size_hint_y=0.35 , halign='center')
        layout.add_widget(lab1)
        print(len(self.values))
        if(len(self.values)==0):
            boxlayout = self.ids['box_menu']
            btn = self.ids['button_add']
            boxlayout.remove_widget(btn)

   def reset(self):
       self.values = list(range(1, 91))
       layout = self.ids['values']
       layout.clear_widgets()
       btn = self.ids['button_add']
       boxlayout = self.ids['box_menu']
       boxlayout.remove_widget(btn)
       boxlayout.add_widget(btn)
class BingoApp(App):
    def build(self):
        return BingoGame()


if __name__ == '__main__':

    BingoApp().run()