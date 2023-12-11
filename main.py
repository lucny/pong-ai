from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.core.window import Window
from game import PongGame
import random
from kivy.core.text import LabelBase

# registering our new custom fontstyle
LabelBase.register(name='Monoton', fn_regular='fonts/Monoton-Regular.ttf')
LabelBase.register(name='Bungee', fn_regular='fonts/BungeeShade-Regular.ttf')
LabelBase.register(name='Fredericka', fn_regular='fonts/FrederickatheGreat-Regular.ttf')


class MenuScreen(Screen):
    STATES = ['ARG', 'AUS', 'AUT', 'BEL', 'BLR', 'BRA', 'BUL', 'CAN', 'COL', 'CRO', 'CUB', 'CZE', 'DEN', 'EGY', 'ESP',
              'EST', 'FIN', 'FRA', 'GBR', 'GER', 'GRE', 'HUN', 'CHN', 'IND', 'IRL', 'IRN', 'ISL', 'ISR', 'ITA', 'JAP',
              'KOR', 'LAT', 'LIT', 'MAR', 'MEX', 'NED', 'NGR', 'NOR', 'NZL', 'PAK', 'POL', 'POR', 'ROM', 'RUS', 'SLO',
              'SRB', 'SUI', 'SVK', 'SWE', 'TUN', 'TUR', 'UKR', 'URU', 'USA']
    left_index = random.randrange(0, int(len(STATES) / 2))
    right_index = random.randrange(int(len(STATES) / 2), len(STATES))


class CanvasScreen(Screen):
    def start_game(self):
        try:
            if not self.manager.playing[0]:
                self.manager.models[0] = None
            if not self.manager.playing[1]:
                self.manager.models[1] = None
            self.game = PongGame(self.manager.models)
        except:
            self.manager.models = [None, None]
            self.game = PongGame(self.manager.models)

        self.add_widget(self.game)
        self.game.start()

class PongApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(CanvasScreen(name='canvas'))
        Config.set('graphics', 'width', '800')
        Config.set('graphics', 'height', '600')
        Config.set('graphics', 'resizable', False)
        Config.write()
        Window.size = (800, 600)

        return sm


PongApp().run()