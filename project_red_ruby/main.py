from game.ui.main_menu import MainMenu
from game.controllers.game_loop import GameLoop


def main():
    # Starte das Hauptmenü des Spiels
    main_menu = MainMenu()
    if main_menu.start_game():
        # Wenn der Spieler startet, initialisieren wir die Spielschleife
        game = GameLoop()
        game.run()


if __name__ == "__main__":
    main()
