class GameStats():
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start Alien Invasion in an inactive state.
        self.game_active = False

        # All-time high score loaded from file.
        with open(self.ai_settings.filename) as file_object:
            self.high_score = int(file_object.read())

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
