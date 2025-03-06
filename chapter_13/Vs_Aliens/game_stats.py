class GameStats:
    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings  # Ensure this correctly references settings
        self.reset_stats()

    def reset_stats(self):
        """Reset the game statistics."""
        self.ships_left = self.settings.ship_limit  # Ensure ship_limit exists in Settings