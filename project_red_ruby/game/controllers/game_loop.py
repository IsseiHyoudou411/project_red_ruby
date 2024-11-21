class GameLoop:
    def __init__(self):
        self.running = True

    def run(self):
        # Hauptspielschleife
        while self.running:
            print("Game Loop Running...")
            # Dummy-Beispiel: Die Schleife nach 3 Iterationen stoppen
            for _ in range(3):
                self.update()

            # Stoppen der Schleife
            self.running = False

    def update(self):
        # Aktualisiere den Spielzustand, z.B. Bewegung von Einheiten oder Ressourcenveränderung
        print("Updating game state...")
