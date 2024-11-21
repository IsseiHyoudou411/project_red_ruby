from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from project_red_ruby.game.controllers.game_loop import GameLoop  # Importiere die Spielschleife aus der


# entsprechenden Datei


class MainMenu(BoxLayout):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        self.game_loop = None
        self.orientation = 'vertical'

        # Titel des Spiels
        self.title_label = Label(text="My Strategy Game", font_size='40sp')
        self.add_widget(self.title_label)

        # Start Button
        self.start_button = Button(text="Start Game", font_size='30sp', size_hint=(.5, .2), pos_hint={'center_x': .5})
        self.start_button.bind(on_press=self.start_game)
        self.add_widget(self.start_button)

        # Exit Button
        self.exit_button = Button(text="Exit", font_size='30sp', size_hint=(.5, .2), pos_hint={'center_x': .5})
        self.exit_button.bind(on_press=self.exit_game)
        self.add_widget(self.exit_button)

    def start_game(self, instance=None):
        print("Game Started!")
        # Wechsel zur Spielschleife
        if not self.game_loop:
            self.game_loop = GameLoop()
            self.game_loop.running = True
            Clock.schedule_interval(self.update_game, 1.0 / 60)

    def update_game(self, dt):
        # Spielaktualisierung
        if self.game_loop and self.game_loop.running:
            self.game_loop.update()
        else:
            return False  # Stoppt den Clock Scheduler, wenn das Spiel beendet ist

    def exit_game(self, instance=None):
        print("Game Exited!")
        if self.game_loop:
            self.game_loop.running = False
        App.get_running_app().stop()


# App Klasse um das Hauptmenü zu starten
class MainMenuApp(App):
    def build(self):
        return MainMenu()


if __name__ == "__main__":
    MainMenuApp().run()
