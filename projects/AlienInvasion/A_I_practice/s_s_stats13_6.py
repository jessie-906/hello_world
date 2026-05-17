class GameStats:
    """Track statistics for the game."""
    def __init__(self, s_s):
        """Initialize statistics."""
        self.settings = s_s.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ship_left = self.settings.ship_limit - 0